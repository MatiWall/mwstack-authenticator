// src/hooks/useAuth.ts
import { UserService } from './client';

export async function loginUser(
  email: string,
  password: string,
  redirectURL: string | null,
  setError: (error: string) => void
) {
  try {
    const response = await UserService.loginUserTokenPost({
      username: email,
      password: password,
    },
    
);

    const token = response.access_token;

    if (redirectURL) {
      // Redirect to external app with token
      window.location.href = `${redirectURL}?token=${encodeURIComponent(token)}`;
    } else {
      // Or store in localStorage if you want your own frontend to stay logged in
      localStorage.setItem('token', token);
    }

  } catch (err) {
    console.error('Login failed', err);
    setError('Failed to login');
  }
}

export async function signUpUser(
    email: string,
    password: string,
    confirmPassword: string,
    redirectURL: string,
    setError: (error: string) => void

){
    if (password !== confirmPassword) {
      setError("Passwords do not match");
      return;
    }

    try {
        await UserService.postUserUserRegisterPost({
            email,
            password,
        });

        await loginUser(email, password, redirectURL, setError)
      
      // maybe redirect or show success message
    } catch (err) {
      console.error("Signup failed:", err);
      setError("Signup failed. Please try again.");
    }
}
