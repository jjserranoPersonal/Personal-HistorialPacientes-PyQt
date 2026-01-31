import { useState } from 'react';
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';
import { Plus, Calendar, User } from 'lucide-react';
import { eventosApi, pacientesApi } from '@/services/api';
import Modal from '@/components/Modal';
import EventoForm from '@/components/EventoForm';
import { format } from 'date-fns';
import { es } from 'date-fns/locale';
import type { EventoCreate } from '@/types';

export default function EventosPage() {
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [selectedPacienteId, setSelectedPacienteId] = useState<number | undefined>();
  const queryClient = useQueryClient();

  const { data: eventos, isLoading, error } = useQuery({
    queryKey: ['eventos'],
    queryFn: () => eventosApi.getAll(),
  });

  const { data: pacientes } = useQuery({
    queryKey: ['pacientes'],
    queryFn: () => pacientesApi.getAll(),
  });

  const createMutation = useMutation({
    mutationFn: (data: EventoCreate) => eventosApi.create(data),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['eventos'] });
      queryClient.invalidateQueries({ queryKey: ['historial'] });
      setIsModalOpen(false);
      setSelectedPacienteId(undefined);
    },
  });

  const handleCreateEvento = async (data: EventoCreate) => {
    await createMutation.mutateAsync(data);
  };

  const handleCloseModal = () => {
    setIsModalOpen(false);
    setSelectedPacienteId(undefined);
  };

  const getPacienteNombre = (pacienteId: number) => {
    const paciente = pacientes?.find(p => p.id === pacienteId);
    return paciente ? `${paciente.nombres} ${paciente.apellidos}` : 'Desconocido';
  };

  return (
    <div className="px-4 py-6 sm:px-0">
      <div className="sm:flex sm:items-center">
        <div className="sm:flex-auto">
          <h1 className="text-2xl font-semibold text-gray-900">Eventos Médicos</h1>
          <p className="mt-2 text-sm text-gray-700">
            Registro de consultas y eventos médicos de los pacientes.
          </p>
        </div>
        <div className="mt-4 sm:mt-0 sm:ml-16 sm:flex-none">
          <button
            type="button"
            onClick={() => setIsModalOpen(true)}
            className="inline-flex items-center justify-center rounded-md border border-transparent bg-indigo-600 px-4 py-2 text-sm font-medium text-white shadow-sm hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2 sm:w-auto"
          >
            <Plus className="mr-2 h-4 w-4" />
            Nuevo Evento
          </button>
        </div>
      </div>

      <div className="mt-8">
        {isLoading ? (
          <div className="text-center py-12">
            <p className="text-gray-500">Cargando eventos...</p>
          </div>
        ) : error ? (
          <div className="text-center py-12">
            <p className="text-red-500">Error al cargar eventos</p>
          </div>
        ) : eventos && eventos.length > 0 ? (
          <div className="space-y-4">
            {eventos.map((evento) => (
              <div
                key={evento.id}
                className="bg-white shadow overflow-hidden sm:rounded-lg hover:shadow-md transition-shadow"
              >
                <div className="px-4 py-5 sm:px-6">
                  <div className="flex items-center justify-between">
                    <div className="flex items-center space-x-3">
                      <div className="flex-shrink-0">
                        <Calendar className="h-6 w-6 text-indigo-600" />
                      </div>
                      <div>
                        <h3 className="text-lg leading-6 font-medium text-gray-900">
                          {evento.motivo_consulta || 'Consulta médica'}
                        </h3>
                        <div className="mt-1 flex items-center text-sm text-gray-500">
                          <User className="h-4 w-4 mr-1" />
                          {getPacienteNombre(evento.paciente_id)}
                        </div>
                      </div>
                    </div>
                    <div className="text-sm text-gray-500">
                      {format(new Date(evento.created_at), "dd/MM/yyyy HH:mm", { locale: es })}
                    </div>
                  </div>
                </div>

                <div className="border-t border-gray-200 px-4 py-5 sm:px-6">
                  <dl className="grid grid-cols-1 gap-x-4 gap-y-4 sm:grid-cols-2">
                    {evento.estado && (
                      <div className="sm:col-span-1">
                        <dt className="text-sm font-medium text-gray-500">Estado</dt>
                        <dd className="mt-1 text-sm text-gray-900">{evento.estado}</dd>
                      </div>
                    )}

                    {evento.imp_diagnostica && (
                      <div className="sm:col-span-1">
                        <dt className="text-sm font-medium text-gray-500">Diagnóstico</dt>
                        <dd className="mt-1 text-sm text-gray-900">{evento.imp_diagnostica}</dd>
                      </div>
                    )}

                    {evento.hea && (
                      <div className="sm:col-span-2">
                        <dt className="text-sm font-medium text-gray-500">Historia de Enfermedad Actual</dt>
                        <dd className="mt-1 text-sm text-gray-900">{evento.hea}</dd>
                      </div>
                    )}

                    {evento.conducta_seguir && (
                      <div className="sm:col-span-2">
                        <dt className="text-sm font-medium text-gray-500">Tratamiento</dt>
                        <dd className="mt-1 text-sm text-gray-900">{evento.conducta_seguir}</dd>
                      </div>
                    )}

                    {(evento.temperatura || evento.tension_arterial || evento.fre_cardiaca || evento.oxigenacion) && (
                      <div className="sm:col-span-2">
                        <dt className="text-sm font-medium text-gray-500 mb-2">Signos Vitales</dt>
                        <dd className="mt-1 flex flex-wrap gap-4 text-sm text-gray-900">
                          {evento.temperatura && (
                            <span className="inline-flex items-center px-3 py-1 rounded-full text-xs font-medium bg-red-100 text-red-800">
                              🌡️ {evento.temperatura}°C
                            </span>
                          )}
                          {evento.tension_arterial && (
                            <span className="inline-flex items-center px-3 py-1 rounded-full text-xs font-medium bg-blue-100 text-blue-800">
                              💉 {evento.tension_arterial}
                            </span>
                          )}
                          {evento.fre_cardiaca && (
                            <span className="inline-flex items-center px-3 py-1 rounded-full text-xs font-medium bg-pink-100 text-pink-800">
                              ❤️ {evento.fre_cardiaca} lpm
                            </span>
                          )}
                          {evento.fre_respiratoria && (
                            <span className="inline-flex items-center px-3 py-1 rounded-full text-xs font-medium bg-green-100 text-green-800">
                              🫁 {evento.fre_respiratoria} rpm
                            </span>
                          )}
                          {evento.oxigenacion && (
                            <span className="inline-flex items-center px-3 py-1 rounded-full text-xs font-medium bg-cyan-100 text-cyan-800">
                              💨 SpO2: {evento.oxigenacion}%
                            </span>
                          )}
                        </dd>
                      </div>
                    )}
                  </dl>
                </div>
              </div>
            ))}
          </div>
        ) : (
          <div className="text-center py-12 bg-white rounded-lg shadow">
            <Calendar className="mx-auto h-12 w-12 text-gray-400" />
            <h3 className="mt-2 text-sm font-medium text-gray-900">No hay eventos registrados</h3>
            <p className="mt-1 text-sm text-gray-500">Comienza registrando un nuevo evento médico.</p>
            <div className="mt-6">
              <button
                type="button"
                onClick={() => setIsModalOpen(true)}
                className="inline-flex items-center px-4 py-2 border border-transparent shadow-sm text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
              >
                <Plus className="-ml-1 mr-2 h-5 w-5" />
                Nuevo Evento
              </button>
            </div>
          </div>
        )}
      </div>

      <Modal
        isOpen={isModalOpen}
        onClose={handleCloseModal}
        title="Registrar Evento Médico"
        size="xl"
      >
        <div className="mb-4">
          <label htmlFor="paciente_select" className="block text-sm font-medium text-gray-700 mb-2">
            Seleccionar Paciente *
          </label>
          <select
            id="paciente_select"
            value={selectedPacienteId || ''}
            onChange={(e) => setSelectedPacienteId(Number(e.target.value))}
            className="block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm px-3 py-2 border"
          >
            <option value="">Seleccionar paciente...</option>
            {pacientes?.map((paciente) => (
              <option key={paciente.id} value={paciente.id}>
                {paciente.identificacion} - {paciente.nombres} {paciente.apellidos}
              </option>
            ))}
          </select>
        </div>

        {selectedPacienteId && (
          <EventoForm
            onSubmit={handleCreateEvento}
            onCancel={handleCloseModal}
            pacienteId={selectedPacienteId}
          />
        )}

        {!selectedPacienteId && (
          <div className="text-center py-8 text-gray-500">
            Por favor, selecciona un paciente para continuar
          </div>
        )}
      </Modal>
    </div>
  );
}
