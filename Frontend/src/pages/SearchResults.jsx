import { useEffect, useState } from "react";
import { Link, useSearchParams } from "react-router-dom";

import SearchBar from "../components/SearchBar";
import VideoResult from "../components/VideoResult";
import { searchVideos } from "../services/api";

function SearchResults() {
  const [searchParams] = useSearchParams();

  const query = searchParams.get("q") || "";

  const [videos, setVideos] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    async function loadVideos() {
      if (!query) {
        setVideos([]);
        setLoading(false);
        return;
      }

      try {
        setLoading(true);
        setError("");

        const data = await searchVideos(query);

        setVideos(data.results);
      } catch (err) {
        console.error(err);

        setError("Something went wrong while searching.");
      } finally {
        setLoading(false);
      }
    }

    loadVideos();
  }, [query]);

  return (
    <main className="results-page">
      <header className="results-header">
        <Link className="small-logo" to="/">
          LearnTube
        </Link>

        <div className="header-search">
          <SearchBar initialValue={query} />
        </div>
      </header>

      <section className="results-container">
        <p className="results-label">
          Top results
        </p>

        <h1 className="results-title">
          {query}
        </h1>

        {loading && (
          <p className="status-message">
            Searching...
          </p>
        )}

        {error && (
          <p className="status-message">
            {error}
          </p>
        )}

        {!loading && !error && videos.length === 0 && (
          <p className="status-message">
            No videos found.
          </p>
        )}

        {!loading && !error && videos.length > 0 && (
          <div className="results-list">
            {videos.map((video) => (
              <VideoResult
                key={video.video_id}
                video={video}
              />
            ))}
          </div>
        )}
      </section>
    </main>
  );
}

export default SearchResults;