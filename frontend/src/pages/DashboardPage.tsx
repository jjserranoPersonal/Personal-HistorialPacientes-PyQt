import { useAuthStore } from '@/stores/authStore';
import { useQuery } from '@tanstack/react-query';
import { pacientesApi, eventosApi } from '@/services/api';
import { Users, FileText, Calendar, Activity } from 'lucide-react';

export default function DashboardPage() {
  const user = useAuthStore((state) => state.user);

  const { data: pacientes } = useQuery({
    queryKey: ['pacientes'],
    queryFn: () => pacientesApi.getAll(),
  });

  const { data: eventos } = useQuery({
    queryKey: ['eventos'],
    queryFn: () => eventosApi.getAll(),
  });

  const totalPacientes = pacientes?.length || 0;
  const totalEventos = eventos?.length || 0;

  const stats = [
    {
      name: 'Total Pacientes',
      value: totalPacientes,
      icon: Users,
      color: 'bg-blue-500',
    },
    {
      name: 'Eventos Registrados',
      value: totalEventos,
      icon: FileText,
      color: 'bg-green-500',
    },
    {
      name: 'Rol',
      value: user?.rol || 'Usuario',
      icon: Activity,
      color: 'bg-indigo-500',
    },
  ];

  return (
    <div className="px-4 py-6 sm:px-0">
      <div className="mb-6">
        <h2 className="text-2xl font-bold text-gray-900">
          Bienvenido, {user?.nombre_completo || user?.usuario}
        </h2>
        <p className="mt-1 text-sm text-gray-600">
          Sistema de gestión de historiales clínicos de pacientes
        </p>
      </div>

      <div className="grid grid-cols-1 gap-5 sm:grid-cols-2 lg:grid-cols-3">
        {stats.map((stat) => {
          const Icon = stat.icon;
          return (
            <div key={stat.name} className="bg-white overflow-hidden shadow rounded-lg">
              <div className="p-5">
                <div className="flex items-center">
                  <div className={`flex-shrink-0 rounded-md p-3 ${stat.color}`}>
                    <Icon className="h-6 w-6 text-white" />
                  </div>
                  <div className="ml-5 w-0 flex-1">
                    <dl>
                      <dt className="text-sm font-medium text-gray-500 truncate">
                        {stat.name}
                      </dt>
                      <dd className="text-2xl font-semibold text-gray-900">
                        {typeof stat.value === 'string' ? (
                          <span className="capitalize">{stat.value}</span>
                        ) : (
                          stat.value
                        )}
                      </dd>
                    </dl>
                  </div>
                </div>
              </div>
            </div>
          );
        })}
      </div>

      <div className="mt-8 grid grid-cols-1 gap-5 lg:grid-cols-2">
        <div className="bg-white overflow-hidden shadow rounded-lg">
          <div className="p-5">
            <h3 className="text-lg font-medium text-gray-900 mb-4">Accesos Rápidos</h3>
            <div className="space-y-3">
              <a
                href="/pacientes"
                className="flex items-center p-3 rounded-lg hover:bg-gray-50 transition-colors"
              >
                <Users className="h-5 w-5 text-indigo-600 mr-3" />
                <span className="text-sm font-medium text-gray-900">Ver Pacientes</span>
              </a>
              <a
                href="/pacientes"
                className="flex items-center p-3 rounded-lg hover:bg-gray-50 transition-colors"
              >
                <FileText className="h-5 w-5 text-indigo-600 mr-3" />
                <span className="text-sm font-medium text-gray-900">Nuevo Paciente</span>
              </a>
            </div>
          </div>
        </div>

        <div className="bg-white overflow-hidden shadow rounded-lg">
          <div className="p-5">
            <h3 className="text-lg font-medium text-gray-900 mb-4">Información del Usuario</h3>
            <dl className="space-y-2">
              <div>
                <dt className="text-sm font-medium text-gray-500">Usuario</dt>
                <dd className="text-sm text-gray-900">{user?.usuario}</dd>
              </div>
              <div>
                <dt className="text-sm font-medium text-gray-500">Email</dt>
                <dd className="text-sm text-gray-900">{user?.email}</dd>
              </div>
              <div>
                <dt className="text-sm font-medium text-gray-500">Rol</dt>
                <dd className="text-sm text-gray-900 capitalize">{user?.rol}</dd>
              </div>
            </dl>
          </div>
        </div>
      </div>
    </div>
  );
}
