import type { Metadata } from "next";
import { Geist, Geist_Mono } from "next/font/google";
import "./globals.css";

const geistSans = Geist({
  variable: "--font-geist-sans",
  subsets: ["latin"],
});

const geistMono = Geist_Mono({
  variable: "--font-geist-mono",
  subsets: ["latin"],
});

export const metadata: Metadata = {
  title: "RetailIQ | Customer Intelligence Platform",

  description:
    "AI-powered retail analytics platform featuring customer segmentation, churn prediction, revenue analytics, KPI dashboards, PDF reporting, and business intelligence insights.",

  keywords: [
    "Retail Analytics",
    "Customer Intelligence",
    "Business Intelligence",
    "Churn Prediction",
    "Customer Segmentation",
    "FastAPI",
    "Next.js",
    "Machine Learning",
    "RetailIQ",
  ],

  authors: [
    {
      name: "Tirthankar Ghosh",
    },
  ],
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html
      lang="en"
      className={`${geistSans.variable} ${geistMono.variable} h-full antialiased`}
    >
      <body className="min-h-full flex flex-col">{children}</body>
    </html>
  );
}
