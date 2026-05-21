export default function LoginPage() {
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
            <h2 className="text-4xl font-bold">Log In</h2>
            <p className="mt-3 text-gray-600">Enter your credentials.</p>

            <form className="mt-8 space-y-5">
              <input
                type="text"
                placeholder="Email or Username"
                className="w-full rounded-2xl border p-4"
              />

              <input
                type="password"
                placeholder="Password"
                className="w-full rounded-2xl border p-4"
              />

              <button
                type="submit"
                className="w-full rounded-2xl bg-violet-600 p-4 text-white"
              >
                Log In
              </button>
            </form>

            <p className="mt-6 text-center text-gray-600">
              No account?{" "}
              <a href="/signup" className="text-violet-600 font-semibold">
                Sign up
              </a>
            </p>
          </div>
        </div>
      </div>
    </main>
  )
}