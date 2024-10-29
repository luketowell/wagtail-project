export default async function BlogIndex() {
  const posts = [
    {
      id: 1,
      title: "First Post",
      date: "2024-02-02",
      intro: "This is the first post",
      meta: {
        slug: "first post",
      },
    },
    {
      id: 2,
      title: "Second Post",
      date: "2024-02-03",
      intro: "This is the Second post",
      meta: {
        slug: "Second post",
      },
    },
  ];

  return (
    <main>
      <div className="mb-8">
        <h1 className="text-4xl font-bold mb-2">Blog</h1>
        <div>
          <p>Some Introduction</p>
        </div>
      </div>
      <ul>
        {posts.map((child) => (
          <li key={child.id} className="mb-4">
            <a className="underline" href={`blog/${child.meta.slug}`}>
              <h2>{child.title}</h2>
            </a>
            <time dateTime={child.date}>
              {new Date(child.date).toDateString()}
            </time>
            <p>{child.intro}</p>
          </li>
        ))}
      </ul>
    </main>
  );
}
