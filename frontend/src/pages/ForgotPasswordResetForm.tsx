import React, { useState } from 'react';
import { Box, Button, TextField } from '@mui/material';
import { useSearchParams } from 'react-router-dom';

import { resetPasswordWithToken } from '../utils';

const ForgotPasswordResetForm: React.FC = () => {
  const [error, setError] = useState('');
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');

  const [searchParams] = useSearchParams();

  
  
  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    // TODO: call backend to send reset email
    const token = searchParams.get('token');

    if (!token) {
      setError("Missing token");
      return;
    }
    await resetPasswordWithToken(token, password, confirmPassword, setError);

  }; 

  return (
    <Box component="form" onSubmit={handleSubmit}>
      <TextField 
        label="Password" 
        type="password" 
        fullWidth 
        margin="normal" 
        value={password} 
        onChange={e => setPassword(e.target.value)} 
      />
      <TextField 
        label="Confirm Password" 
        type="password" 
        fullWidth 
        margin="normal" 
        value={confirmPassword} 
        onChange={e => setConfirmPassword(e.target.value)} 
      />
      <Button type="submit" variant="contained" color="primary" fullWidth sx={{ mt: 2 }}>
        Update Password
      </Button>
            {error && (
              <Box color="error.main" mt={1}>
                {error}
              </Box>
            )}
    </Box>
  );
};

export default ForgotPasswordResetForm;
