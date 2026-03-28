import React, { useState } from 'react';
import { Box, Button, TextField, Link } from '@mui/material';
import { useSearchParams } from 'react-router-dom';

import { sendPasswordResetEmail } from '../utils';

const ForgotPasswordForm: React.FC = () => {
  const [email, setEmail] = useState('');
  const [error, setError] = useState<string | null>('');
  const [searchParams] = useSearchParams();
  const redirectURL = searchParams.get('redirect_url');

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    // TODO: call backend to send reset email
    await sendPasswordResetEmail(email, setError);
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
      {error && (
        <Box color="error.main" mt={1}>
          {error}
        </Box>
      )}
      <Button type="submit" variant="contained" color="primary" fullWidth sx={{ mt: 2 }}>
        Send Reset Link
      </Button>
        <Box style={{marginTop: '0.5rem'}}>
            <Link href={`/login?redirect_url=${redirectURL}`} style={{'marginRight': '0.7rem'}} underline='hover'>Login</Link>
            <Link href={`/login/reset?redirect_url=${redirectURL}`} underline='hover'>Reset Password</Link>
      </Box>
    </Box>
  );
};

export default ForgotPasswordForm;
