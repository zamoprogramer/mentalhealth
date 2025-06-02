import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { ThemeProvider, CssBaseline } from '@mui/material';
import theme from './theme';
import Home from './pages/Home';
import Login from './pages/Login';
import Register from './pages/Register';
import { LanguageProvider } from './context/LanguageContext';
import LanguageToggle from './components/LanguageToggle';

function App() {
  return (
    <LanguageProvider>
      <ThemeProvider theme={theme}>
        <CssBaseline />
        <Router>
          <LanguageToggle />
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/login" element={<Login />} />
            <Route path="/register" element={<Register />} />
            {/* Aquí agregaremos más rutas cuando creemos las otras páginas */}
          </Routes>
        </Router>
      </ThemeProvider>
    </LanguageProvider>
  );
}

export default App;
