import React, { useState } from 'react';
import { Box, Button, TextField, Link } from '@mui/material';
import { signUpUser } from '../utils';
import { useSearchParams } from 'react-router-dom';


const SignupForm: React.FC = () => {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [confirmPassword, setConfirmPassword] = useState('');
    const [error, setError] = useState<string | null>(null);
    
    const [searchParams] = useSearchParams();
    const redirectURL = searchParams.get('redirect_url');
    console.log(redirectURL);
    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        if (!redirectURL){
            setError('No redirect url.');
            return
        }else {
            setError('');
        }
        await signUpUser(email, password, confirmPassword, redirectURL, setError);
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
        label="Confirm Password"
        type="password"
        fullWidth
        margin="normal"
        value={confirmPassword}
        onChange={e => setConfirmPassword(e.target.value)}
      />
      {error && (
        <Box color="error.main" mt={1}>
          {error}
        </Box>
      )}
      <Button type="submit" variant="contained" color="primary" fullWidth sx={{ mt: 2 }}>
        Sign Up
      </Button>
      <Box mt={1}>
        <Link href="/login/" underline="hover">
          Already have an account? Login
        </Link>
      </Box>
    </Box>
  );
};

export default SignupForm;
