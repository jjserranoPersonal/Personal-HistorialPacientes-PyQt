import { useState } from 'react';
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';
import { Search, Plus, Edit, Trash2 } from 'lucide-react';
import { pacientesApi } from '@/services/api';
import Modal from '@/components/Modal';
import PacienteForm from '@/components/PacienteForm';
import ConfirmDialog from '@/components/ConfirmDialog';
import type { PacienteCreate, Paciente } from '@/types';

export default function PacientesPage() {
  const [searchTerm, setSearchTerm] = useState('');
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [isDeleteDialogOpen, setIsDeleteDialogOpen] = useState(false);
  const [selectedPaciente, setSelectedPaciente] = useState<Paciente | null>(null);
  const [isEditMode, setIsEditMode] = useState(false);
  const queryClient = useQueryClient();

  const { data: pacientes, isLoading, error } = useQuery({
    queryKey: ['pacientes', searchTerm],
    queryFn: () => pacientesApi.getAll({ nombre: searchTerm }),
  });

  const createMutation = useMutation({
    mutationFn: (data: PacienteCreate) => pacientesApi.create(data),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['pacientes'] });
      setIsModalOpen(false);
      setSelectedPaciente(null);
    },
  });

  const updateMutation = useMutation({
    mutationFn: ({ id, data }: { id: number; data: PacienteCreate }) =>
      pacientesApi.update(id, data),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['pacientes'] });
      setIsModalOpen(false);
      setSelectedPaciente(null);
      setIsEditMode(false);
    },
  });

  const deleteMutation = useMutation({
    mutationFn: (id: number) => pacientesApi.delete(id),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['pacientes'] });
      setIsDeleteDialogOpen(false);
      setSelectedPaciente(null);
    },
  });

  const handleCreatePaciente = async (data: PacienteCreate) => {
    if (isEditMode && selectedPaciente) {
      await updateMutation.mutateAsync({ id: selectedPaciente.id, data });
    } else {
      await createMutation.mutateAsync(data);
    }
  };

  const handleEditClick = (paciente: Paciente) => {
    setSelectedPaciente(paciente);
    setIsEditMode(true);
    setIsModalOpen(true);
  };

  const handleDeleteClick = (paciente: Paciente) => {
    setSelectedPaciente(paciente);
    setIsDeleteDialogOpen(true);
  };

  const handleConfirmDelete = async () => {
    if (selectedPaciente) {
      await deleteMutation.mutateAsync(selectedPaciente.id);
    }
  };

  const handleCloseModal = () => {
    setIsModalOpen(false);
    setSelectedPaciente(null);
    setIsEditMode(false);
  };

  return (
    <div className="px-4 py-6 sm:px-0">
      <div className="sm:flex sm:items-center">
        <div className="sm:flex-auto">
          <h1 className="text-2xl font-semibold text-gray-900">Pacientes</h1>
          <p className="mt-2 text-sm text-gray-700">
            Listado de todos los pacientes registrados en el sistema.
          </p>
        </div>
        <div className="mt-4 sm:mt-0 sm:ml-16 sm:flex-none">
          <button
            type="button"
            onClick={() => setIsModalOpen(true)}
            className="inline-flex items-center justify-center rounded-md border border-transparent bg-indigo-600 px-4 py-2 text-sm font-medium text-white shadow-sm hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2 sm:w-auto"
          >
            <Plus className="mr-2 h-4 w-4" />
            Nuevo Paciente
          </button>
        </div>
      </div>

      <div className="mt-6">
        <input
          type="text"
          placeholder="Buscar por nombre..."
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
          className="block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm"
        />
      </div>

      <div className="mt-8 flex flex-col">
        <div className="-my-2 -mx-4 overflow-x-auto sm:-mx-6 lg:-mx-8">
          <div className="inline-block min-w-full py-2 align-middle md:px-6 lg:px-8">
            <div className="overflow-hidden shadow ring-1 ring-black ring-opacity-5 md:rounded-lg">
              {isLoading ? (
                <div className="text-center py-12">
                  <p className="text-gray-500">Cargando pacientes...</p>
                </div>
              ) : error ? (
                <div className="text-center py-12">
                  <p className="text-red-500">Error al cargar pacientes</p>
                </div>
              ) : (
                <table className="min-w-full divide-y divide-gray-300">
                  <thead className="bg-gray-50">
                    <tr>
                      <th className="py-3.5 pl-4 pr-3 text-left text-sm font-semibold text-gray-900 sm:pl-6">
                        Identificación
                      </th>
                      <th className="px-3 py-3.5 text-left text-sm font-semibold text-gray-900">
                        Nombres
                      </th>
                      <th className="px-3 py-3.5 text-left text-sm font-semibold text-gray-900">
                        Apellidos
                      </th>
                      <th className="px-3 py-3.5 text-left text-sm font-semibold text-gray-900">
                        Teléfono
                      </th>
                      <th className="relative py-3.5 pl-3 pr-4 sm:pr-6">
                        <span className="sr-only">Acciones</span>
                      </th>
                    </tr>
                  </thead>
                  <tbody className="divide-y divide-gray-200 bg-white">
                    {pacientes && pacientes.length > 0 ? (
                      pacientes.map((paciente) => (
                        <tr key={paciente.id}>
                          <td className="whitespace-nowrap py-4 pl-4 pr-3 text-sm font-medium text-gray-900 sm:pl-6">
                            {paciente.identificacion}
                          </td>
                          <td className="whitespace-nowrap px-3 py-4 text-sm text-gray-500">
                            {paciente.nombres}
                          </td>
                          <td className="whitespace-nowrap px-3 py-4 text-sm text-gray-500">
                            {paciente.apellidos}
                          </td>
                          <td className="whitespace-nowrap px-3 py-4 text-sm text-gray-500">
                            {paciente.telefono || '-'}
                          </td>
                          <td className="relative whitespace-nowrap py-4 pl-3 pr-4 text-right text-sm font-medium sm:pr-6">
                            <div className="flex justify-end space-x-2">
                              <button
                                onClick={() => handleEditClick(paciente)}
                                className="text-indigo-600 hover:text-indigo-900"
                                title="Editar"
                              >
                                <Edit className="h-4 w-4" />
                              </button>
                              <button
                                onClick={() => handleDeleteClick(paciente)}
                                className="text-red-600 hover:text-red-900"
                                title="Eliminar"
                              >
                                <Trash2 className="h-4 w-4" />
                              </button>
                            </div>
                          </td>
                        </tr>
                      ))
                    ) : (
                      <tr>
                        <td colSpan={5} className="px-3 py-8 text-center text-sm text-gray-500">
                          No se encontraron pacientes
                        </td>
                      </tr>
                    )}
                  </tbody>
                </table>
              )}
            </div>
          </div>
        </div>
      </div>

      <Modal
        isOpen={isModalOpen}
        onClose={handleCloseModal}
        title={isEditMode ? 'Editar Paciente' : 'Nuevo Paciente'}
        size="lg"
      >
        <PacienteForm
          onSubmit={handleCreatePaciente}
          onCancel={handleCloseModal}
          initialData={selectedPaciente || undefined}
          isEdit={isEditMode}
        />
      </Modal>

      <ConfirmDialog
        isOpen={isDeleteDialogOpen}
        onClose={() => setIsDeleteDialogOpen(false)}
        onConfirm={handleConfirmDelete}
        title="Eliminar Paciente"
        message={`¿Está seguro que desea eliminar al paciente ${selectedPaciente?.nombres} ${selectedPaciente?.apellidos}? Esta acción no se puede deshacer.`}
        confirmText="Eliminar"
        cancelText="Cancelar"
        isLoading={deleteMutation.isPending}
      />
    </div>
  );
}
