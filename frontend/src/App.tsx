import { Box, Container, Typography, useTheme } from '@mui/material';
import { LoginForm, ResetPasswordForm, ForgotPasswordForm, SignupForm } from './pages';
import { BrowserRouter, Routes, Route } from 'react-router-dom';



function App() {

  const theme = useTheme();


  return (

    <Box style={{width: '100vw', height: '100vh', padding: 0, margin: 0, background: theme.palette.background.paper}}>
            <Container maxWidth="sm" sx={{ mt: 8 }}>
          <Box textAlign="center" mb={2}>
            <Typography variant="h4">FitTracker Auth</Typography>
          </Box>

        <BrowserRouter>
          <Routes>
            <Route path='/login/' element={<LoginForm/>}/>
            <Route path='/login/reset/' element={<ResetPasswordForm/>}/>
            <Route path='/login/forgot/' element={<ForgotPasswordForm/>}/>
            <Route path='/login/signup/' element={<SignupForm/>}/>
          </Routes>
        </BrowserRouter>
        </Container>
    </Box>
  );
}

export default App;
