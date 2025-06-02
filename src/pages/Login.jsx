import { useState } from 'react';
import { 
  Box, 
  Container, 
  Paper, 
  Typography, 
  TextField, 
  Button, 
  Link,
  InputAdornment,
  IconButton,
  Alert
} from '@mui/material';
import { Visibility, VisibilityOff } from '@mui/icons-material';
import { useNavigate } from 'react-router-dom';
import { useLanguage } from '../context/LanguageContext';
import { translations } from '../utils/translations';
import { login } from '../services/authService';

const Login = () => {
  const navigate = useNavigate();
  const { language } = useLanguage();
  const t = translations[language].login;
  const [showPassword, setShowPassword] = useState(false);
  const [formData, setFormData] = useState({
    email: '',
    password: ''
  });
  const [error, setError] = useState('');

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    
    try {
      await login(formData.email, formData.password);
      navigate('/dashboard'); // Redirigir al dashboard después del login exitoso
    } catch (error) {
      setError(error.message);
    }
  };

  return (
    <Box
      sx={{
        minHeight: '100vh',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        background: 'linear-gradient(45deg, #000000 30%, #1a1a1a 90%)',
      }}
    >
      <Container maxWidth="md">
        <Paper
          elevation={3}
          sx={{
            p: 6,
            backgroundColor: 'rgba(26, 26, 26, 0.9)',
            backdropFilter: 'blur(10px)',
            borderRadius: 2,
            maxWidth: '600px',
            margin: '0 auto',
            boxShadow: '0 8px 32px rgba(0, 0, 0, 0.3)'
          }}
        >
          <Typography variant="h4" color="primary" gutterBottom align="center">
            {t.title}
          </Typography>
          
          {error && (
            <Alert severity="error" sx={{ mb: 2 }}>
              {error}
            </Alert>
          )}

          <Box component="form" onSubmit={handleSubmit} sx={{ mt: 3 }}>
            <TextField
              fullWidth
              label={t.email}
              name="email"
              type="email"
              value={formData.email}
              onChange={handleChange}
              required
              variant="outlined"
              color="primary"
              sx={{ mb: 2 }}
            />
            <TextField
              fullWidth
              label={t.password}
              name="password"
              type={showPassword ? 'text' : 'password'}
              value={formData.password}
              onChange={handleChange}
              required
              variant="outlined"
              color="primary"
              InputProps={{
                endAdornment: (
                  <InputAdornment position="end">
                    <IconButton
                      onClick={() => setShowPassword(!showPassword)}
                      edge="end"
                    >
                      {showPassword ? <VisibilityOff /> : <Visibility />}
                    </IconButton>
                  </InputAdornment>
                ),
              }}
              sx={{ mb: 3 }}
            />

            <Button
              type="submit"
              fullWidth
              variant="contained"
              color="primary"
              size="large"
              sx={{ 
                mb: 2,
                background: 'linear-gradient(45deg, #2196f3 30%, #21CBF3 90%)',
                '&:hover': {
                  background: 'linear-gradient(45deg, #1976d2 30%, #1E88E5 90%)',
                }
              }}
            >
              {t.submit}
            </Button>

            <Box sx={{ textAlign: 'center', mt: 2 }}>
              <Typography variant="body2" color="text.secondary">
                {t.noAccount}{' '}
                <Link
                  component="button"
                  variant="body2"
                  color="primary"
                  onClick={() => navigate('/register')}
                  sx={{ textDecoration: 'none' }}
                >
                  {t.registerHere}
                </Link>
              </Typography>
            </Box>
          </Box>
        </Paper>
      </Container>
    </Box>
  );
};

export default Login; 