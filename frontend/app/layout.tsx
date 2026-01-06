import "../styles/globals.css";
import Navbar from "./components/Navbar";
import Footer from "./components/Footer";

export const metadata = {
  title: "Sohail Shaik | Data Platform Engineer",
  description:
    "Data Platform & MDM Engineer specializing in Stibo STEP, Azure AI, SAP/Excel integrations and global product data platforms.",
  keywords: [
    "Data Platform Engineer",
    "MDM Engineer",
    "Stibo STEP",
    "Azure AI",
    "Data Integration",
    "Analytics Engineer",
    "Sohail Shaik",
  ],
  openGraph: {
    title: "Sohail Shaik | Data Platform Engineer",
    description:
      "Enterprise Data Platform & MDM Engineer working on global product data platforms at Diageo.",
    url: "https://sohailshaik.dev",
    siteName: "Sohail Portfolio",
    images: [
      {
        url: "/profile.png",
        width: 800,
        height: 600,
        alt: "Sohail Shaik",
      },
    ],
    type: "website",
  },
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body className="page">
        <Navbar />
        <main className="content">{children}</main>
        <Footer />
      </body>
    </html>
  );
}
