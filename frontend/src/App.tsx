import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import { useAuthStore } from '@/stores/authStore';
import LoginPage from '@/pages/LoginPage';
import DashboardPage from '@/pages/DashboardPage';
import PacientesPage from '@/pages/PacientesPage';
import Layout from '@/components/Layout';

const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      refetchOnWindowFocus: false,
      retry: 1,
    },
  },
});

function ProtectedRoute({ children }: { children: React.ReactNode }) {
  const isAuthenticated = useAuthStore((state) => state.isAuthenticated);
  const token = useAuthStore((state) => state.token);
  const user = useAuthStore((state) => state.user);
  
  console.log('🛡️ ProtectedRoute evaluando acceso:');
  console.log('  - isAuthenticated:', isAuthenticated);
  console.log('  - token:', token ? token.substring(0, 20) + '...' : 'null');
  console.log('  - user:', user);
  
  // Verificar token en localStorage como fallback
  const localToken = localStorage.getItem('token');
  console.log('  - localStorage token:', localToken ? localToken.substring(0, 20) + '...' : 'null');
  
  if (!isAuthenticated && !token && !localToken) {
    console.log('❌ No autenticado, redirigiendo a login');
    return <Navigate to="/login" replace />;
  }
  
  console.log('✅ Autenticado, mostrando contenido protegido');
  return <>{children}</>;
}

function App() {
  return (
    <QueryClientProvider client={queryClient}>
      <BrowserRouter>
        <Routes>
          <Route path="/login" element={<LoginPage />} />
          <Route
            path="/"
            element={
              <ProtectedRoute>
                <Layout />
              </ProtectedRoute>
            }
          >
            <Route index element={<DashboardPage />} />
            <Route path="pacientes" element={<PacientesPage />} />
          </Route>
        </Routes>
      </BrowserRouter>
    </QueryClientProvider>
  );
}

export default App;
