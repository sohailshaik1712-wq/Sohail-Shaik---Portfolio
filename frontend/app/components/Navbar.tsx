import Link from "next/link";

export default function Navbar() {
  return (
    <nav className="nav">
      <h3>Sohail Shaik</h3>
      <div>
        <Link href="/">Home</Link>
        <Link href="/about">About</Link>
        <Link href="/projects">Projects</Link>
        <Link href="/contact">Contact</Link>
      </div>
    </nav>
  );
}
