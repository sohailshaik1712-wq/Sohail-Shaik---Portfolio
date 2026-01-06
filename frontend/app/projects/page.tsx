import Image from "next/image";

import { Project } from "@/types/project";

export default async function Projects() {
  const res = await fetch(
    "https://sohail-shaik-portfolio.onrender.com/projects",
    {
      cache: "no-store",
    },
  );
  const projects: Project[] = await res.json();

  return (
    <section>
      <h1>Enterprise Projects</h1>
      <div className="grid">
        {projects.map((p) => (
          <a key={p.slug} href={`/projects/${p.slug}`} className="card">
            <Image
              src={p.image}
              alt={p.title}
              width={400}
              height={200}
              className="card-img"
            />
            <h3>{p.title}</h3>
            <p>{p.description}</p>
            <div className="tags">
              {p.tags.split(",").map((t) => (
                <span key={t}>{t}</span>
              ))}
            </div>
          </a>
        ))}
      </div>
    </section>
  );
}
