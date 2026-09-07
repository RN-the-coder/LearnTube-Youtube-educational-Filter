import { Link, useLocation, useParams } from "react-router-dom";

function Watch() {
  const { videoId } = useParams();
  const location = useLocation();

  const video = location.state?.video;

  return (
    <main className="watch-page">
      <header className="watch-header">
        <Link className="small-logo" to="/">
          LearnTube
        </Link>

        <button
          className="back-button"
          onClick={() => window.history.back()}
        >
          Back
        </button>
      </header>

      <section className="watch-container">
        <div className="player-wrapper">
          <iframe
            src={`https://www.youtube.com/embed/${videoId}?rel=0`}
            title={video?.title || "LearnTube video"}
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
            allowFullScreen
          />
        </div>

        {video && (
          <div className="watch-info">
            <h1>
              {video.title}
            </h1>

            <p>
              {video.channel}
            </p>
          </div>
        )}
      </section>
    </main>
  );
}

export default Watch;