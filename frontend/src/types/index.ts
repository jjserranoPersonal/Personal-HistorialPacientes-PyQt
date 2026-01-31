export interface Usuario {
  id: number;
  usuario: string;
  email: string;
  nombre_completo?: string;
  rol: string;
  activo: boolean;
  created_at: string;
  updated_at: string;
}

export interface Paciente {
  id: number;
  identificacion: string;
  nombres: string;
  apellidos: string;
  direccion?: string;
  correo?: string;
  telefono?: string;
  fecha_nacimiento?: string;
  sexo?: string;
  transfusiones?: string;
  peso?: string;
  talla?: string;
  habitos_toxicos?: string;
  alergia_medicamentos?: string;
  vacunacion?: string;
  app?: string;
  apf?: string;
  nombre_acompanante?: string;
  foto_url?: string;
  created_at: string;
  updated_at: string;
  created_by?: number;
}

export interface PacienteCreate {
  identificacion: string;
  nombres: string;
  apellidos: string;
  direccion?: string;
  correo?: string;
  telefono?: string;
  fecha_nacimiento?: string;
  sexo?: string;
  transfusiones?: string;
  peso?: string;
  talla?: string;
  habitos_toxicos?: string;
  alergia_medicamentos?: string;
  vacunacion?: string;
  app?: string;
  apf?: string;
  nombre_acompanante?: string;
  contacto_emergencia?: string;
  telefono_emergencia?: string;
}

export interface Evento {
  id: number;
  paciente_id: number;
  estado?: string;
  hea?: string;
  imp_diagnostica?: string;
  conducta_seguir?: string;
  motivo_consulta?: string;
  temperatura?: string;
  tension_arterial?: string;
  fre_cardiaca?: string;
  fre_respiratoria?: string;
  oxigenacion?: string;
  created_at: string;
  created_by?: number;
}

export interface EventoCreate {
  paciente_id: number;
  estado?: string;
  hea?: string;
  imp_diagnostica?: string;
  conducta_seguir?: string;
  motivo_consulta?: string;
  temperatura?: string;
  tension_arterial?: string;
  fre_cardiaca?: string;
  fre_respiratoria?: string;
  oxigenacion?: string;
}

export interface LoginRequest {
  username: string;
  password: string;
}

export interface LoginResponse {
  access_token: string;
  token_type: string;
}
