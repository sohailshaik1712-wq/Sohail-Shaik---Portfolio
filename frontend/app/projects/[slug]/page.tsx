import Image from "next/image";
import { notFound } from "next/navigation";
import { Project } from "@/types/project";

interface PageProps {
  params: {
    slug: string;
  };
}

export default async function ProjectDetail({ params }: PageProps) {
  const res = await fetch(
    `https://sohail-shaik-portfolio.onrender.com/projects/${params.slug}`,
    {
      cache: "no-store",
    },
  );

  if (!res.ok) return notFound();

  const project: Project | null = await res.json();

  if (!project) return notFound();

  return (
    <section>
      <Image
        src={project.image}
        alt={project.title}
        width={400}
        height={200}
        className="card-img"
      />
      <h1>{project.title}</h1>
      <p>{project.details}</p>
      <div className="tags">
        {project.tags.split(",").map((t) => (
          <span key={t}>{t}</span>
        ))}
      </div>
    </section>
  );
}
