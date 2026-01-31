import { useForm } from 'react-hook-form';
import { zodResolver } from '@hookform/resolvers/zod';
import { z } from 'zod';
import { useState } from 'react';
import type { EventoCreate } from '@/types';

const eventoSchema = z.object({
  paciente_id: z.number().min(1, 'El paciente es requerido'),
  estado: z.string().optional(),
  hea: z.string().optional(),
  imp_diagnostica: z.string().optional(),
  conducta_seguir: z.string().optional(),
  motivo_consulta: z.string().optional(),
  temperatura: z.string().optional(),
  tension_arterial: z.string().optional(),
  fre_cardiaca: z.string().optional(),
  fre_respiratoria: z.string().optional(),
  oxigenacion: z.string().optional(),
});

type EventoFormData = z.infer<typeof eventoSchema>;

interface EventoFormProps {
  onSubmit: (data: EventoCreate) => Promise<void>;
  onCancel: () => void;
  pacienteId?: number;
  initialData?: Partial<EventoCreate>;
}

export default function EventoForm({ onSubmit, onCancel, pacienteId, initialData }: EventoFormProps) {
  const [isSubmitting, setIsSubmitting] = useState(false);

  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm<EventoFormData>({
    resolver: zodResolver(eventoSchema),
    defaultValues: {
      paciente_id: pacienteId || initialData?.paciente_id,
      ...initialData,
    } as EventoFormData,
  });

  const onFormSubmit = async (data: EventoFormData) => {
    setIsSubmitting(true);
    try {
      await onSubmit(data as EventoCreate);
    } finally {
      setIsSubmitting(false);
    }
  };

  return (
    <form onSubmit={handleSubmit(onFormSubmit)} className="space-y-6">
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        <div className="md:col-span-2">
          <label htmlFor="motivo_consulta" className="block text-sm font-medium text-gray-700">
            Motivo de Consulta
          </label>
          <textarea
            {...register('motivo_consulta')}
            rows={2}
            className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm px-3 py-2 border"
            placeholder="Ej: Dolor abdominal, fiebre..."
          />
        </div>

        <div className="md:col-span-2">
          <label htmlFor="estado" className="block text-sm font-medium text-gray-700">
            Estado del Paciente
          </label>
          <textarea
            {...register('estado')}
            rows={2}
            className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm px-3 py-2 border"
            placeholder="Ej: Paciente consciente, orientado..."
          />
        </div>

        <div className="md:col-span-2">
          <label htmlFor="hea" className="block text-sm font-medium text-gray-700">
            Historia de Enfermedad Actual (HEA)
          </label>
          <textarea
            {...register('hea')}
            rows={3}
            className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm px-3 py-2 border"
            placeholder="Descripción detallada de la enfermedad actual..."
          />
        </div>

        <div className="md:col-span-2">
          <label htmlFor="imp_diagnostica" className="block text-sm font-medium text-gray-700">
            Impresión Diagnóstica
          </label>
          <textarea
            {...register('imp_diagnostica')}
            rows={2}
            className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm px-3 py-2 border"
            placeholder="Ej: Gastritis aguda, Hipertensión arterial..."
          />
        </div>

        <div className="md:col-span-2">
          <label htmlFor="conducta_seguir" className="block text-sm font-medium text-gray-700">
            Conducta a Seguir / Tratamiento
          </label>
          <textarea
            {...register('conducta_seguir')}
            rows={3}
            className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm px-3 py-2 border"
            placeholder="Ej: Omeprazol 20mg cada 12h, reposo..."
          />
        </div>

        <div className="md:col-span-2 border-t pt-4">
          <h4 className="text-sm font-medium text-gray-900 mb-3">Signos Vitales</h4>
          <div className="grid grid-cols-2 md:grid-cols-3 gap-4">
            <div>
              <label htmlFor="temperatura" className="block text-sm font-medium text-gray-700">
                Temperatura (°C)
              </label>
              <input
                {...register('temperatura')}
                type="text"
                className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm px-3 py-2 border"
                placeholder="36.5"
              />
            </div>

            <div>
              <label htmlFor="tension_arterial" className="block text-sm font-medium text-gray-700">
                Tensión Arterial
              </label>
              <input
                {...register('tension_arterial')}
                type="text"
                className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm px-3 py-2 border"
                placeholder="120/80"
              />
            </div>

            <div>
              <label htmlFor="fre_cardiaca" className="block text-sm font-medium text-gray-700">
                Frecuencia Cardíaca
              </label>
              <input
                {...register('fre_cardiaca')}
                type="text"
                className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm px-3 py-2 border"
                placeholder="72 lpm"
              />
            </div>

            <div>
              <label htmlFor="fre_respiratoria" className="block text-sm font-medium text-gray-700">
                Frecuencia Respiratoria
              </label>
              <input
                {...register('fre_respiratoria')}
                type="text"
                className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm px-3 py-2 border"
                placeholder="16 rpm"
              />
            </div>

            <div>
              <label htmlFor="oxigenacion" className="block text-sm font-medium text-gray-700">
                Saturación O2 (%)
              </label>
              <input
                {...register('oxigenacion')}
                type="text"
                className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm px-3 py-2 border"
                placeholder="98"
              />
            </div>
          </div>
        </div>
      </div>

      <div className="flex justify-end space-x-3 pt-4 border-t">
        <button
          type="button"
          onClick={onCancel}
          disabled={isSubmitting}
          className="px-4 py-2 border border-gray-300 rounded-md shadow-sm text-sm font-medium text-gray-700 bg-white hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 disabled:opacity-50"
        >
          Cancelar
        </button>
        <button
          type="submit"
          disabled={isSubmitting}
          className="px-4 py-2 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 disabled:opacity-50"
        >
          {isSubmitting ? 'Guardando...' : 'Registrar Evento'}
        </button>
      </div>
    </form>
  );
}
