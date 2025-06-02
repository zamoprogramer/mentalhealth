import { Box, Container, Typography, Button, Grid, Paper } from '@mui/material';
import { useNavigate } from 'react-router-dom';
import { useLanguage } from '../context/LanguageContext';
import { translations } from '../utils/translations';

const Home = () => {
  const navigate = useNavigate();
  const { language } = useLanguage();
  const t = translations[language].home;

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
      {/* Efecto de partículas o gradiente en el fondo */}
      <Box
        sx={{
          position: 'absolute',
          top: 0,
          left: 0,
          right: 0,
          bottom: 0,
          background: 'radial-gradient(circle at center, rgba(33, 150, 243, 0.1) 0%, transparent 70%)',
          pointerEvents: 'none',
        }}
      />

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
          <Box sx={{ textAlign: 'center', mb: 6 }}>
            <Typography 
              variant="h2" 
              color="primary" 
              gutterBottom
              sx={{
                textShadow: '0 0 20px rgba(33, 150, 243, 0.3)',
                fontWeight: 'bold',
                mb: 3
              }}
            >
              {t.title}
            </Typography>
            <Typography 
              variant="h5" 
              color="text.secondary" 
              paragraph
              sx={{ 
                mb: 4,
                maxWidth: '600px',
                margin: '0 auto'
              }}
            >
              {t.subtitle}
            </Typography>
          </Box>
          
          <Paper 
            elevation={3} 
            sx={{ 
              p: 4, 
              backgroundColor: 'rgba(26, 26, 26, 0.8)',
              backdropFilter: 'blur(10px)',
              borderRadius: 2,
              maxWidth: '500px',
              margin: '0 auto'
            }}
          >
            <Typography 
              variant="h6" 
              color="primary" 
              gutterBottom
              sx={{ textAlign: 'center', mb: 3 }}
            >
              {t.ready}
            </Typography>
            <Box sx={{ 
              display: 'flex', 
              gap: 2, 
              justifyContent: 'center',
              flexWrap: 'wrap'
            }}>
              <Button
                variant="contained"
                color="primary"
                size="large"
                onClick={() => navigate('/login')}
                sx={{ 
                  minWidth: '200px',
                  background: 'linear-gradient(45deg, #2196f3 30%, #21CBF3 90%)',
                  '&:hover': {
                    background: 'linear-gradient(45deg, #1976d2 30%, #1E88E5 90%)',
                  }
                }}
              >
                {t.login}
              </Button>
              <Button
                variant="outlined"
                color="primary"
                size="large"
                onClick={() => navigate('/register')}
                sx={{ 
                  minWidth: '200px',
                  borderWidth: 2,
                  '&:hover': {
                    borderWidth: 2,
                  }
                }}
              >
                {t.register}
              </Button>
            </Box>
          </Paper>
        </Paper>
      </Container>
    </Box>
  );
};

export default Home; 