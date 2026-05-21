export default function SignupPage() {
  return (
    <main className="flex min-h-screen items-center justify-center bg-gradient-to-b from-slate-100 to-white px-6 py-12">
      <div className="grid w-full max-w-6xl overflow-hidden rounded-[32px] bg-white shadow-2xl lg:grid-cols-2">

        {/* Left Panel */}
        <div className="hidden flex-col justify-between bg-violet-600 p-12 text-white lg:flex">
          <div>
            <h1 className="text-5xl font-extrabold">Create Account</h1>
            <p className="mt-6 text-violet-100">
              Register to access barangay services online.
            </p>
          </div>

          <div className="space-y-4">
            <div className="rounded-2xl bg-white/10 p-4">
              Request documents online
            </div>
            <div className="rounded-2xl bg-white/10 p-4">
              Receive announcements instantly
            </div>
          </div>
        </div>

        {/* Right Panel */}
        <div className="flex items-center justify-center p-8 lg:p-16">
          <div className="w-full max-w-md">
            <h2 className="text-4xl font-bold">Register</h2>
            <p className="mt-3 text-gray-600">Create your account.</p>

            <form className="mt-8 space-y-5">
              <input className="w-full rounded-2xl border p-4" placeholder="Full Name" />
              <input className="w-full rounded-2xl border p-4" placeholder="Address" />
              <input className="w-full rounded-2xl border p-4" placeholder="Contact Number" />
              <input className="w-full rounded-2xl border p-4" placeholder="Email" />
              <input className="w-full rounded-2xl border p-4" placeholder="Password" />

              <input type="file" className="w-full border p-4 rounded-2xl" />

              <button className="w-full rounded-2xl bg-violet-600 p-4 text-white">
                Sign Up
              </button>
            </form>

            <p className="mt-6 text-center text-gray-600">
              Already have an account?{" "}
              <a href="/login" className="text-violet-600 font-semibold">
                Login
              </a>
            </p>
          </div>
        </div>
      </div>
    </main>
  )
}   