'use client';

import { useState } from 'react';

export default function LoginPage() {
  const [identifier, setIdentifier] = useState(''); 
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const [isLoading, setIsLoading] = useState(false);

  const handleLogin = async (e: React.FormEvent) => {
    e.preventDefault(); 
    setError('');
    setIsLoading(true);

    if (!identifier || !password) {
      setError('Please fill in all fields.');
      setIsLoading(false);
      return;
    }

    try {
      console.log('Sending credentials to backend:', { identifier, password });
      
      await new Promise((resolve) => setTimeout(resolve, 1500));

      if (identifier === 'admin' && password === 'password123') {
        alert('Login successful! Redirecting...');
      } else {
        setError('Invalid username/email or password.');
      }
    } catch (err) {
      setError('Something went wrong. Please try again later.');
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <main className="flex min-h-screen items-center justify-center bg-gradient-to-b from-slate-100 to-white px-6 py-12">
      <div className="grid w-full max-w-6xl overflow-hidden rounded-[32px] bg-white shadow-2xl lg:grid-cols-2">
        
        {/* Left Panel */}
        <div className="hidden flex-col justify-between bg-violet-600 p-12 text-white lg:flex">
          <div>
            <h1 className="text-5xl font-extrabold">Welcome Back</h1>
            <p className="mt-6 text-violet-100">
              Access your Barangay Information System account.
            </p>
          </div>

          <div className="space-y-4">
            <div className="rounded-2xl bg-white/10 p-4">
              Secure resident records
            </div>
            <div className="rounded-2xl bg-white/10 p-4">
              Track requests and announcements
            </div>
          </div>
        </div>

        {/* Right Panel */}
        <div className="flex items-center justify-center p-8 lg:p-16">
          <div className="w-full max-w-md">
            <h2 className="text-4xl font-bold text-black">Log In</h2>
            <p className="mt-3 text-gray-600">Enter your credentials.</p>

            {/* 4. Display an error alert if authentication fails */}
            {error && (
              <div className="mt-4 rounded-xl bg-red-50 p-4 text-sm text-red-600 font-medium">
                {error}
              </div>
            )}

            {/* 5. Connect the form submit handler */}
            <form onSubmit={handleLogin} className="mt-8 space-y-5 text-black">
              <input 
                type="text" 
                placeholder="Email or Username" 
                value={identifier}
                onChange={(e) => setIdentifier(e.target.value)} // Update state on type
                className="w-full rounded-2xl border p-4 focus:outline-violet-600"
                disabled={isLoading}
              />
              <input 
                type="password" 
                placeholder="Password" 
                value={password}
                onChange={(e) => setPassword(e.target.value)} // Update state on type
                className="w-full rounded-2xl border p-4 focus:outline-violet-600"
                disabled={isLoading}
              />

              {/* 6. Dynamic button states for a better user experience */}
              <button 
                type="submit" 
                className="w-full rounded-2xl bg-violet-600 p-4 text-white hover:bg-violet-700 transition font-semibold disabled:bg-violet-400"
                disabled={isLoading}
              >
                {isLoading ? 'Logging in...' : 'Log In'}
              </button>
            </form>

            <p className="mt-6 text-center text-gray-600">
              No account?{" "}
              <a href="/signup" className="text-violet-600 font-semibold hover:underline">
                Sign up
              </a>
            </p>
          </div>
        </div>
      </div>
    </main>
  );
}