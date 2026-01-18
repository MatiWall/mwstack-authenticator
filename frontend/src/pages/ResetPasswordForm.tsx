import React, { useState } from 'react';
import { Box, Button, TextField, Link } from '@mui/material';

const ResetPasswordForm: React.FC = () => {
  const [newPassword, setNewPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (newPassword !== confirmPassword) {
      alert('Passwords do not match');
      return;
    }
    // TODO: call backend to reset password
    console.log({ newPassword });
  };

  return (
    <Box component="form" onSubmit={handleSubmit}>
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
        <Box style={{marginTop: '0.5rem'}}>
            <Link href='/login/' style={{'marginRight': '0.7rem'}} underline='hover'>Login</Link>
            <Link href='/login/forgot/' underline='hover'>Forgot Password?</Link>
      </Box>
    </Box>
  );
};

export default ResetPasswordForm;
