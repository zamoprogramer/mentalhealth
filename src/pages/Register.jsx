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
  MenuItem,
  Grid,
  Alert
} from '@mui/material';
import { Visibility, VisibilityOff } from '@mui/icons-material';
import { useNavigate } from 'react-router-dom';
import { useLanguage } from '../context/LanguageContext';
import { translations } from '../utils/translations';
import { register } from '../services/authService';

const Register = () => {
  const navigate = useNavigate();
  const { language } = useLanguage();
  const t = translations[language].register;
  const [showPassword, setShowPassword] = useState(false);
  const [error, setError] = useState('');
  const [formData, setFormData] = useState({
    firstName: '',
    lastName: '',
    country: '',
    email: '',
    password: ''
  });

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
      await register(formData);
      navigate('/login'); // Redirigir al login después del registro exitoso
    } catch (error) {
      setError(error.message);
    }
  };

  // Lista de países (puedes expandirla según necesites)
  const countries = [
    'Colombia',
    'México',
    'España',
    'Argentina',
    'Chile',
    'Perú',
    'Ecuador',
    'Venezuela',
    'Otro'
  ];

  return (
    <Box
      sx={{
        minHeight: '100vh',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        background: 'linear-gradient(45deg, #000000 30%, #1a1a1a 90%)',
        py: 4
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
            maxWidth: '800px',
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
            <Grid container spacing={2}>
              <Grid item xs={12} sm={6}>
                <TextField
                  fullWidth
                  label={t.firstName}
                  name="firstName"
                  value={formData.firstName}
                  onChange={handleChange}
                  required
                  variant="outlined"
                  color="primary"
                />
              </Grid>
              <Grid item xs={12} sm={6}>
                <TextField
                  fullWidth
                  label={t.lastName}
                  name="lastName"
                  value={formData.lastName}
                  onChange={handleChange}
                  required
                  variant="outlined"
                  color="primary"
                />
              </Grid>
              <Grid item xs={12}>
                <TextField
                  fullWidth
                  select
                  label={t.country}
                  name="country"
                  value={formData.country}
                  onChange={handleChange}
                  required
                  variant="outlined"
                  color="primary"
                >
                  {countries.map((country) => (
                    <MenuItem key={country} value={country}>
                      {country}
                    </MenuItem>
                  ))}
                </TextField>
              </Grid>
              <Grid item xs={12}>
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
                />
              </Grid>
              <Grid item xs={12}>
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
                  helperText={t.passwordHelper}
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
                />
              </Grid>
            </Grid>

            <Button
              type="submit"
              fullWidth
              variant="contained"
              color="primary"
              size="large"
              sx={{ 
                mt: 3,
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
                {t.haveAccount}{' '}
                <Link
                  component="button"
                  variant="body2"
                  color="primary"
                  onClick={() => navigate('/login')}
                  sx={{ textDecoration: 'none' }}
                >
                  {t.loginHere}
                </Link>
              </Typography>
            </Box>
          </Box>
        </Paper>
      </Container>
    </Box>
  );
};

export default Register; 