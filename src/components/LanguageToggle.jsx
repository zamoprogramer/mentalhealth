import { IconButton, Tooltip } from '@mui/material';
import { Translate } from '@mui/icons-material';
import { useLanguage } from '../context/LanguageContext';

const LanguageToggle = () => {
  const { language, toggleLanguage } = useLanguage();

  return (
    <Tooltip title={language === 'es' ? 'Switch to English' : 'Cambiar a Español'}>
      <IconButton
        onClick={toggleLanguage}
        sx={{
          position: 'fixed',
          top: 20,
          right: 20,
          backgroundColor: 'rgba(33, 150, 243, 0.1)',
          '&:hover': {
            backgroundColor: 'rgba(33, 150, 243, 0.2)',
          },
        }}
      >
        <Translate />
      </IconButton>
    </Tooltip>
  );
};

export default LanguageToggle; 