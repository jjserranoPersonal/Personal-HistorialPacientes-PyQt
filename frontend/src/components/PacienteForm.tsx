import { useForm } from 'react-hook-form';
import { zodResolver } from '@hookform/resolvers/zod';
import { z } from 'zod';
import { useState } from 'react';
import type { PacienteCreate } from '@/types';

const pacienteSchema = z.object({
  identificacion: z.string().min(1, 'La identificación es requerida'),
  nombres: z.string().min(1, 'Los nombres son requeridos'),
  apellidos: z.string().min(1, 'Los apellidos son requeridos'),
  fecha_nacimiento: z.string().min(1, 'La fecha de nacimiento es requerida'),
  genero: z.enum(['M', 'F', 'Otro'], { required_error: 'El género es requerido' }),
  telefono: z.string().optional(),
  email: z.string().email('Email inválido').optional().or(z.literal('')),
  direccion: z.string().optional(),
  contacto_emergencia: z.string().optional(),
  telefono_emergencia: z.string().optional(),
});

type PacienteFormData = z.infer<typeof pacienteSchema>;

interface PacienteFormProps {
  onSubmit: (data: PacienteCreate) => Promise<void>;
  onCancel: () => void;
  initialData?: Partial<PacienteCreate>;
  isEdit?: boolean;
}

export default function PacienteForm({ onSubmit, onCancel, initialData, isEdit = false }: PacienteFormProps) {
  const [isSubmitting, setIsSubmitting] = useState(false);

  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm<PacienteFormData>({
    resolver: zodResolver(pacienteSchema),
    defaultValues: initialData,
  });

  const onFormSubmit = async (data: PacienteFormData) => {
    setIsSubmitting(true);
    try {
      await onSubmit(data as PacienteCreate);
    } finally {
      setIsSubmitting(false);
    }
  };

  return (
    <form onSubmit={handleSubmit(onFormSubmit)} className="space-y-6">
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        <div>
          <label htmlFor="identificacion" className="block text-sm font-medium text-gray-700">
            Identificación *
          </label>
          <input
            {...register('identificacion')}
            type="text"
            className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm px-3 py-2 border"
            placeholder="Ej: 1234567890"
          />
          {errors.identificacion && (
            <p className="mt-1 text-sm text-red-600">{errors.identificacion.message}</p>
          )}
        </div>

        <div>
          <label htmlFor="genero" className="block text-sm font-medium text-gray-700">
            Género *
          </label>
          <select
            {...register('genero')}
            className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm px-3 py-2 border"
          >
            <option value="">Seleccionar...</option>
            <option value="M">Masculino</option>
            <option value="F">Femenino</option>
            <option value="Otro">Otro</option>
          </select>
          {errors.genero && (
            <p className="mt-1 text-sm text-red-600">{errors.genero.message}</p>
          )}
        </div>

        <div>
          <label htmlFor="nombres" className="block text-sm font-medium text-gray-700">
            Nombres *
          </label>
          <input
            {...register('nombres')}
            type="text"
            className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm px-3 py-2 border"
            placeholder="Ej: Juan Carlos"
          />
          {errors.nombres && (
            <p className="mt-1 text-sm text-red-600">{errors.nombres.message}</p>
          )}
        </div>

        <div>
          <label htmlFor="apellidos" className="block text-sm font-medium text-gray-700">
            Apellidos *
          </label>
          <input
            {...register('apellidos')}
            type="text"
            className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm px-3 py-2 border"
            placeholder="Ej: Pérez García"
          />
          {errors.apellidos && (
            <p className="mt-1 text-sm text-red-600">{errors.apellidos.message}</p>
          )}
        </div>

        <div>
          <label htmlFor="fecha_nacimiento" className="block text-sm font-medium text-gray-700">
            Fecha de Nacimiento *
          </label>
          <input
            {...register('fecha_nacimiento')}
            type="date"
            className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm px-3 py-2 border"
          />
          {errors.fecha_nacimiento && (
            <p className="mt-1 text-sm text-red-600">{errors.fecha_nacimiento.message}</p>
          )}
        </div>

        <div>
          <label htmlFor="telefono" className="block text-sm font-medium text-gray-700">
            Teléfono
          </label>
          <input
            {...register('telefono')}
            type="tel"
            className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm px-3 py-2 border"
            placeholder="Ej: 0999999999"
          />
          {errors.telefono && (
            <p className="mt-1 text-sm text-red-600">{errors.telefono.message}</p>
          )}
        </div>

        <div className="md:col-span-2">
          <label htmlFor="email" className="block text-sm font-medium text-gray-700">
            Email
          </label>
          <input
            {...register('email')}
            type="email"
            className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm px-3 py-2 border"
            placeholder="Ej: paciente@email.com"
          />
          {errors.email && (
            <p className="mt-1 text-sm text-red-600">{errors.email.message}</p>
          )}
        </div>

        <div className="md:col-span-2">
          <label htmlFor="direccion" className="block text-sm font-medium text-gray-700">
            Dirección
          </label>
          <input
            {...register('direccion')}
            type="text"
            className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm px-3 py-2 border"
            placeholder="Ej: Av. Principal 123 y Calle Secundaria"
          />
        </div>

        <div>
          <label htmlFor="contacto_emergencia" className="block text-sm font-medium text-gray-700">
            Contacto de Emergencia
          </label>
          <input
            {...register('contacto_emergencia')}
            type="text"
            className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm px-3 py-2 border"
            placeholder="Ej: María Pérez (Madre)"
          />
        </div>

        <div>
          <label htmlFor="telefono_emergencia" className="block text-sm font-medium text-gray-700">
            Teléfono de Emergencia
          </label>
          <input
            {...register('telefono_emergencia')}
            type="tel"
            className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm px-3 py-2 border"
            placeholder="Ej: 0999999999"
          />
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
          {isSubmitting ? 'Guardando...' : isEdit ? 'Actualizar' : 'Crear Paciente'}
        </button>
      </div>
    </form>
  );
}
