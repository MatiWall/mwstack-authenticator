import React, { useState } from 'react';
import { Box, Button, TextField, Link } from '@mui/material';
import { useSearchParams } from 'react-router-dom';
import { loginUser } from '../utils';




const LoginForm: React.FC = () => {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');

    const [searchParams] = useSearchParams();
    const redirectURL = searchParams.get('redirect_url');

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        await loginUser(email, password, redirectURL, setError);
    };

  return (
    <Box component="form" onSubmit={handleSubmit}>
      <TextField 
        label="Email" 
        fullWidth 
        margin="normal" 
        value={email} 
        onChange={e => setEmail(e.target.value)} 
      />
      <TextField 
        label="Password" 
        type="password" 
        fullWidth 
        margin="normal" 
        value={password} 
        onChange={e => setPassword(e.target.value)} 
      />
      <Button type="submit" variant="contained" color="primary" fullWidth sx={{ mt: 2 }}>
        Login
      </Button>
            {error && (
              <Box color="error.main" mt={1}>
                {error}
              </Box>
            )}
      <Box style={{marginTop: '0.5rem'}}>
        <Link href='/login/forgot' style={{'marginRight': '0.7rem'}} underline='hover'>Forgot Password?</Link>
        <Link href='/login/reset' style={{'marginRight': '0.7rem'}} underline='hover'>Reset Password</Link>
        <Link href='/login/signup' underline='hover'>Signup</Link>
      </Box>
    </Box>
  );
};

export default LoginForm;
