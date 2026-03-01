import React, { useState } from 'react';
import { Box, Button, TextField, Link } from '@mui/material';
import { useSearchParams } from 'react-router-dom';

const ForgotPasswordForm: React.FC = () => {
  const [email, setEmail] = useState('');

  const [searchParams] = useSearchParams();
  const redirectURL = searchParams.get('redirect_url');

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    // TODO: call backend to send reset email
    console.log({ email });
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
