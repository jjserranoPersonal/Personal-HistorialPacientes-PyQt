import axios from 'axios';
import type { LoginRequest, LoginResponse, Usuario, Paciente, PacienteCreate, Evento, EventoCreate } from '@/types';

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

const api = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Interceptor para agregar token a las peticiones
api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('token');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

// Interceptor para manejar errores de autenticación
api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      localStorage.removeItem('token');
      localStorage.removeItem('user');
      window.location.href = '/login';
    }
    return Promise.reject(error);
  }
);

// Auth
export const authApi = {
  login: async (credentials: LoginRequest): Promise<LoginResponse> => {
    const formData = new URLSearchParams();
    formData.append('username', credentials.username);
    formData.append('password', credentials.password);
    
    const response = await api.post<LoginResponse>('/api/v1/auth/login', formData, {
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
      },
    });
    return response.data;
  },
  
  getMe: async (): Promise<Usuario> => {
    const response = await api.get<Usuario>('/api/v1/auth/me');
    return response.data;
  },
};

// Pacientes
export const pacientesApi = {
  getAll: async (params?: { skip?: number; limit?: number; nombre?: string; identificacion?: string }): Promise<Paciente[]> => {
    const response = await api.get<Paciente[]>('/api/v1/pacientes', { params });
    return response.data;
  },
  
  getById: async (id: number): Promise<Paciente> => {
    const response = await api.get<Paciente>(`/api/v1/pacientes/${id}`);
    return response.data;
  },
  
  create: async (paciente: PacienteCreate): Promise<Paciente> => {
    const response = await api.post<Paciente>('/api/v1/pacientes', paciente);
    return response.data;
  },
  
  update: async (id: number, paciente: Partial<PacienteCreate>): Promise<Paciente> => {
    const response = await api.put<Paciente>(`/api/v1/pacientes/${id}`, paciente);
    return response.data;
  },
  
  delete: async (id: number): Promise<void> => {
    await api.delete(`/api/v1/pacientes/${id}`);
  },
};

// Eventos
export const eventosApi = {
  getAll: async (params?: { skip?: number; limit?: number; paciente_id?: number }): Promise<Evento[]> => {
    const response = await api.get<Evento[]>('/api/v1/eventos', { params });
    return response.data;
  },
  
  getById: async (id: number): Promise<Evento> => {
    const response = await api.get<Evento>(`/api/v1/eventos/${id}`);
    return response.data;
  },
  
  create: async (evento: EventoCreate): Promise<Evento> => {
    const response = await api.post<Evento>('/api/v1/eventos', evento);
    return response.data;
  },
  
  getHistorial: async (pacienteId: number): Promise<Evento[]> => {
    const response = await api.get<Evento[]>(`/api/v1/eventos/pacientes/${pacienteId}/historial`);
    return response.data;
  },
};

export default api;
