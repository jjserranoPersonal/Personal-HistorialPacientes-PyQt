import { useParams, useNavigate } from 'react-router-dom';
import { useQuery } from '@tanstack/react-query';
import { pacientesApi, eventosApi } from '@/services/api';
import { ArrowLeft, Calendar, Phone, Mail, MapPin, User, FileText } from 'lucide-react';
import { format } from 'date-fns';
import { es } from 'date-fns/locale';

export default function PacienteDetallePage() {
  const { id } = useParams<{ id: string }>();
  const navigate = useNavigate();

  const { data: paciente, isLoading: loadingPaciente } = useQuery({
    queryKey: ['paciente', id],
    queryFn: () => pacientesApi.getById(Number(id)),
    enabled: !!id,
  });

  const { data: historial, isLoading: loadingHistorial } = useQuery({
    queryKey: ['historial', id],
    queryFn: () => eventosApi.getHistorial(Number(id)),
    enabled: !!id,
  });

  if (loadingPaciente) {
    return (
      <div className="flex justify-center items-center min-h-screen">
        <p className="text-gray-500">Cargando información del paciente...</p>
      </div>
    );
  }

  if (!paciente) {
    return (
      <div className="flex justify-center items-center min-h-screen">
        <p className="text-red-500">Paciente no encontrado</p>
      </div>
    );
  }

  const calcularEdad = (fechaNacimiento: string) => {
    const hoy = new Date();
    const nacimiento = new Date(fechaNacimiento);
    let edad = hoy.getFullYear() - nacimiento.getFullYear();
    const mes = hoy.getMonth() - nacimiento.getMonth();
    if (mes < 0 || (mes === 0 && hoy.getDate() < nacimiento.getDate())) {
      edad--;
    }
    return edad;
  };

  return (
    <div className="px-4 py-6 sm:px-0">
      <button
        onClick={() => navigate('/pacientes')}
        className="mb-4 inline-flex items-center text-sm text-indigo-600 hover:text-indigo-900"
      >
        <ArrowLeft className="h-4 w-4 mr-2" />
        Volver a Pacientes
      </button>

      <div className="bg-white shadow overflow-hidden sm:rounded-lg">
        <div className="px-4 py-5 sm:px-6 bg-gradient-to-r from-indigo-600 to-indigo-800">
          <h3 className="text-2xl leading-6 font-bold text-white">
            {paciente.nombres} {paciente.apellidos}
          </h3>
          <p className="mt-1 max-w-2xl text-sm text-indigo-100">
            Información detallada del paciente
          </p>
        </div>

        <div className="border-t border-gray-200 px-4 py-5 sm:px-6">
          <dl className="grid grid-cols-1 gap-x-4 gap-y-6 sm:grid-cols-2">
            <div className="sm:col-span-1">
              <dt className="text-sm font-medium text-gray-500 flex items-center">
                <User className="h-4 w-4 mr-2" />
                Identificación
              </dt>
              <dd className="mt-1 text-sm text-gray-900">{paciente.identificacion}</dd>
            </div>

            <div className="sm:col-span-1">
              <dt className="text-sm font-medium text-gray-500 flex items-center">
                <Calendar className="h-4 w-4 mr-2" />
                Fecha de Nacimiento
              </dt>
              <dd className="mt-1 text-sm text-gray-900">
                {paciente.fecha_nacimiento
                  ? `${format(new Date(paciente.fecha_nacimiento), 'dd/MM/yyyy', { locale: es })} (${calcularEdad(paciente.fecha_nacimiento)} años)`
                  : '-'}
              </dd>
            </div>

            <div className="sm:col-span-1">
              <dt className="text-sm font-medium text-gray-500">Género</dt>
              <dd className="mt-1 text-sm text-gray-900">
                {paciente.sexo === 'M' ? 'Masculino' : paciente.sexo === 'F' ? 'Femenino' : paciente.sexo || '-'}
              </dd>
            </div>

            <div className="sm:col-span-1">
              <dt className="text-sm font-medium text-gray-500 flex items-center">
                <Phone className="h-4 w-4 mr-2" />
                Teléfono
              </dt>
              <dd className="mt-1 text-sm text-gray-900">{paciente.telefono || '-'}</dd>
            </div>

            <div className="sm:col-span-1">
              <dt className="text-sm font-medium text-gray-500 flex items-center">
                <Mail className="h-4 w-4 mr-2" />
                Email
              </dt>
              <dd className="mt-1 text-sm text-gray-900">{paciente.correo || '-'}</dd>
            </div>

            <div className="sm:col-span-1">
              <dt className="text-sm font-medium text-gray-500 flex items-center">
                <MapPin className="h-4 w-4 mr-2" />
                Dirección
              </dt>
              <dd className="mt-1 text-sm text-gray-900">{paciente.direccion || '-'}</dd>
            </div>
          </dl>
        </div>
      </div>

      <div className="mt-8 bg-white shadow overflow-hidden sm:rounded-lg">
        <div className="px-4 py-5 sm:px-6 border-b border-gray-200">
          <h3 className="text-lg leading-6 font-medium text-gray-900 flex items-center">
            <FileText className="h-5 w-5 mr-2 text-indigo-600" />
            Historial Médico
          </h3>
        </div>

        <div className="px-4 py-5 sm:p-6">
          {loadingHistorial ? (
            <p className="text-gray-500">Cargando historial...</p>
          ) : historial && historial.length > 0 ? (
            <div className="space-y-6">
              {historial.map((evento) => (
                <div key={evento.id} className="border-l-4 border-indigo-500 pl-4 py-2">
                  <div className="flex justify-between items-start mb-2">
                    <h4 className="text-sm font-semibold text-gray-900">
                      {evento.motivo_consulta || 'Consulta médica'}
                    </h4>
                    <span className="text-xs text-gray-500">
                      {format(new Date(evento.created_at), "dd/MM/yyyy HH:mm", { locale: es })}
                    </span>
                  </div>

                  {evento.estado && (
                    <div className="mb-2">
                      <span className="text-xs font-medium text-gray-500">Estado: </span>
                      <span className="text-sm text-gray-900">{evento.estado}</span>
                    </div>
                  )}

                  {evento.imp_diagnostica && (
                    <div className="mb-2">
                      <span className="text-xs font-medium text-gray-500">Diagnóstico: </span>
                      <span className="text-sm text-gray-900">{evento.imp_diagnostica}</span>
                    </div>
                  )}

                  {evento.conducta_seguir && (
                    <div className="mb-2">
                      <span className="text-xs font-medium text-gray-500">Tratamiento: </span>
                      <span className="text-sm text-gray-900">{evento.conducta_seguir}</span>
                    </div>
                  )}

                  {(evento.temperatura || evento.tension_arterial || evento.fre_cardiaca) && (
                    <div className="mt-2 flex flex-wrap gap-4 text-xs text-gray-600">
                      {evento.temperatura && (
                        <span>🌡️ Temp: {evento.temperatura}°C</span>
                      )}
                      {evento.tension_arterial && (
                        <span>💉 TA: {evento.tension_arterial}</span>
                      )}
                      {evento.fre_cardiaca && (
                        <span>❤️ FC: {evento.fre_cardiaca} lpm</span>
                      )}
                      {evento.oxigenacion && (
                        <span>🫁 SpO2: {evento.oxigenacion}%</span>
                      )}
                    </div>
                  )}
                </div>
              ))}
            </div>
          ) : (
            <p className="text-gray-500 text-center py-8">
              No hay eventos registrados para este paciente
            </p>
          )}
        </div>
      </div>
    </div>
  );
}
