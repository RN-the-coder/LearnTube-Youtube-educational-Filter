import { useNavigate } from "react-router-dom";

function VideoResult({ video }) {
  const navigate = useNavigate();

  const handleClick = () => {
    navigate(`/watch/${video.video_id}`, {
      state: {
        video,
      },
    });
  };

  return (
    <article
      className="video-result"
      onClick={handleClick}
    >
      <div className="thumbnail-wrapper">
        <img
          className="video-thumbnail"
          src={video.thumbnail}
          alt={video.title}
        />
      </div>

      <div className="video-info">
        <h2>
          {video.title}
        </h2>

        <p className="video-channel">
          {video.channel}
        </p>

        <p className="video-description">
          {video.description}
        </p>
      </div>
    </article>
  );
}

export default VideoResult;