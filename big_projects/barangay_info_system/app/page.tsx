import Link from "next/link";

export default function HomePage(): JSX.Element {
  return (
    <main className="min-h-screen bg-white text-gray-900">

      {/* HERO */}
      <section className="relative overflow-hidden text-white">

        {/* BACKGROUND IMAGE LAYER */}
        <div className="absolute inset-0">
          <img
            src="/LOGO.jpg"
            alt="Barangay Background"
            className="w-full h-full object-cover opacity-100"
          />
          {/* dark overlay for readability */}
          <div className="absolute inset-0 bg-gradient-to-br from-violet-800/90 via-violet-700/80 to-indigo-700/90" />
        </div>

        {/* CONTENT */}
        <div className="relative z-10 mx-auto max-w-7xl px-6 py-24 flex flex-col lg:flex-row items-center justify-between gap-12">

          {/* LEFT TEXT */}
          <div className="max-w-2xl space-y-6">
            <span className="bg-white/20 px-4 py-2 rounded-full text-sm">
              Barangay Pulong Buhangin Official Portal
            </span>

            <h1 className="text-5xl font-extrabold leading-tight">
              Digital Barangay <br />
              <span className="text-yellow-300">Information System</span>
            </h1>

            <p className="text-white/80 text-lg">
              Access services, request documents, report concerns, and stay updated
              with your barangay—all in one platform.
            </p>

            <div className="flex gap-4 flex-wrap">
              <Link
                href="/login"
                className="bg-white text-violet-700 px-6 py-3 rounded-xl font-semibold hover:bg-gray-100 transition"
              >
                Get Started
              </Link>

              <Link
                href="/signup"
                className="border border-white px-6 py-3 rounded-xl font-semibold hover:bg-white/10 transition"
              >
                Create Account
              </Link>
            </div>
          </div>

          {/* CARDS */}
          <div className="grid grid-cols-2 gap-4 w-full max-w-md">
            {[
              { title: "Residents", desc: "Manage records" },
              { title: "Requests", desc: "Online processing" },
              { title: "Reports", desc: "File complaints" },
              { title: "Health", desc: "Book appointments" },
            ].map((item) => (
              <div
                key={item.title}
                className="bg-white/10 backdrop-blur-md p-5 rounded-2xl border border-white/20"
              >
                <h3 className="font-bold">{item.title}</h3>
                <p className="text-sm text-white/70">{item.desc}</p>
              </div>
            ))}
          </div>

        </div>
      </section>

      {/* STATS */}
      <section className="py-16 bg-gray-50">
        <div className="max-w-7xl mx-auto px-6 grid md:grid-cols-4 gap-6 text-center">

          {[
            { num: "10,000+", label: "Residents" },
            { num: "24/7", label: "Service Access" },
            { num: "100%", label: "Digital Requests" },
            { num: "Fast", label: "Processing" },
          ].map((item) => (
            <div key={item.label} className="bg-white p-6 rounded-2xl shadow">
              <h2 className="text-3xl font-bold text-violet-600">
                {item.num}
              </h2>
              <p className="text-gray-600 mt-2">{item.label}</p>
            </div>
          ))}

        </div>
      </section>

      {/* FEATURES */}
      <section className="py-20">
        <div className="max-w-7xl mx-auto px-6">

          <div className="text-center mb-12">
            <h2 className="text-4xl font-bold">Core Services</h2>
            <p className="text-gray-600 mt-3">
              Everything you need from your barangay in one system
            </p>
          </div>

          <div className="grid md:grid-cols-3 gap-6">
            {[
              "Barangay Clearance Requests",
              "Complaint Reporting System",
              "Resident Information Management",
              "Health Appointment Booking",
              "Announcement Updates",
              "Document Tracking System",
            ].map((service) => (
              <div
                key={service}
                className="p-6 rounded-2xl border bg-white hover:shadow-lg transition"
              >
                <h3 className="font-bold text-lg">{service}</h3>
                <p className="text-sm text-gray-600 mt-2">
                  Easily access {service.toLowerCase()} anytime online.
                </p>
              </div>
            ))}
          </div>

        </div>
      </section>

      {/* CTA */}
      <section className="py-20 bg-violet-700 text-white text-center">
        <div className="max-w-3xl mx-auto px-6 space-y-6">

          <h2 className="text-4xl font-bold">
            Ready to Access Barangay Services Online?
          </h2>

          <p className="text-white/80">
            Create your account today and experience faster, easier, and transparent
            barangay transactions.
          </p>

          <Link
            href="/signup"
            className="inline-block bg-white text-violet-700 px-8 py-4 rounded-xl font-bold hover:bg-gray-100 transition"
          >
            Start Now
          </Link>

        </div>
      </section>

      {/* FOOTER */}
      <footer className="bg-white border-t py-10">
        <div className="max-w-7xl mx-auto px-6 flex flex-col md:flex-row justify-between items-center text-sm text-gray-600">

          <p>© 2026 Barangay Pulong Buhangin Information System</p>

          <div className="flex gap-6 mt-4 md:mt-0">
            <a href="#">About</a>
            <a href="#">Help</a>
            <a href="#">Contact</a>
          </div>

        </div>
      </footer>

    </main>
  );
}