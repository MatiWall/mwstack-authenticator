import React, { useState } from 'react';
import { Box, Button, TextField, Link } from '@mui/material';
import { useSearchParams } from 'react-router-dom';
import { requestPasswordReset } from '../utils';

const ResetPasswordForm: React.FC = () => {
    const [error, setError] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [newPassword, setNewPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');


      const [searchParams] = useSearchParams();
    const redirectURL = searchParams.get('redirect_url');
  if (!redirectURL) {
    return <Box>Missing redirect URL</Box>;
  }

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (newPassword !== confirmPassword) {
      alert('Passwords do not match');
      return;
    }
    await requestPasswordReset(email, password, newPassword, confirmPassword, redirectURL, setError);
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
      <TextField 
        label="New Password" 
        type="password" 
        fullWidth 
        margin="normal" 
        value={newPassword} 
        onChange={e => setNewPassword(e.target.value)} 
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
        Reset Password
      </Button>
        {error && (
        <Box color="error.main" mt={1}>
          {error}
        </Box>
      )}
        <Box style={{marginTop: '0.5rem'}}>
            <Link href={`/login?redirect_url=${redirectURL}`} style={{'marginRight': '0.7rem'}} underline='hover'>Login</Link>
            <Link href={`/login/forgot?redirect_url=${redirectURL}`} underline='hover'>Forgot Password?</Link>
      </Box>
    </Box>
  );
};

export default ResetPasswordForm;
