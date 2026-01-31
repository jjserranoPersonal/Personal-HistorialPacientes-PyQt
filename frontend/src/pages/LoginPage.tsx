import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuthStore } from '@/stores/authStore';
import { authApi } from '@/services/api';

export default function LoginPage() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();
  const setAuth = useAuthStore((state) => state.setAuth);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError('');
    setLoading(true);

    try {
      console.log('=== INICIO LOGIN ===');
      console.log('1. Intentando login con:', { username, password });
      
      const loginResponse = await authApi.login({ username, password });
      console.log('2. Login exitoso, token recibido:', loginResponse);
      
      // IMPORTANTE: Guardar el token ANTES de llamar a getMe
      console.log('3. Guardando token en localStorage...');
      localStorage.setItem('token', loginResponse.access_token);
      
      console.log('4. Obteniendo datos del usuario...');
      const user = await authApi.getMe();
      console.log('5. Usuario obtenido:', user);
      
      console.log('6. Guardando en store...');
      setAuth(user, loginResponse.access_token);
      console.log('7. Auth guardado en store');
      
      console.log('8. Navegando a dashboard...');
      navigate('/', { replace: true });
      
      console.log('9. Navegación completada');
      console.log('=== FIN LOGIN ===');
    } catch (err: any) {
      console.error('=== ERROR EN LOGIN ===');
      console.error('Error completo:', err);
      console.error('Error response:', err.response);
      console.error('Error message:', err.message);
      const errorMessage = err.response?.data?.detail || err.message || 'Error al iniciar sesión. Verifica que el backend esté corriendo en http://localhost:8000';
      setError(errorMessage);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-blue-50 to-indigo-100">
      <div className="max-w-md w-full space-y-8 p-8 bg-white rounded-xl shadow-2xl">
        <div>
          <h2 className="mt-6 text-center text-3xl font-extrabold text-gray-900">
            Historial Pacientes
          </h2>
          <p className="mt-2 text-center text-sm text-gray-600">
            Ingresa tus credenciales para continuar
          </p>
        </div>
        <form className="mt-8 space-y-6" onSubmit={handleSubmit}>
          {error && (
            <div className="rounded-md bg-red-50 p-4">
              <p className="text-sm text-red-800">{error}</p>
            </div>
          )}
          <div className="rounded-md shadow-sm -space-y-px">
            <div>
              <label htmlFor="username" className="sr-only">
                Usuario
              </label>
              <input
                id="username"
                name="username"
                type="text"
                required
                className="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-t-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"
                placeholder="Usuario"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
              />
            </div>
            <div>
              <label htmlFor="password" className="sr-only">
                Contraseña
              </label>
              <input
                id="password"
                name="password"
                type="password"
                required
                className="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-b-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"
                placeholder="Contraseña"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
              />
            </div>
          </div>

          <div>
            <button
              type="submit"
              disabled={loading}
              className="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 disabled:opacity-50"
            >
              {loading ? 'Iniciando sesión...' : 'Iniciar Sesión'}
            </button>
          </div>
          
          <div className="text-sm text-center text-gray-600">
            <p>Usuario de prueba: <strong>jserrano</strong></p>
            <p>Contraseña: <strong>JSerrano2024!Secure</strong></p>
          </div>
        </form>
      </div>
    </div>
  );
}
