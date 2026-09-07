import SearchBar from "../components/SearchBar";

function Home() {
  return (
    <main className="home">
      <section className="home-content">
        <h1 className="brand">LearnTube</h1>

        <p className="tagline">
          Learn from YouTube. Without distractions.
        </p>

        <SearchBar />
      </section>

      <p className="home-footer">Search. Choose. Learn. Made By Ronald Nivar</p>
       
    </main>
  );
}

export default Home;