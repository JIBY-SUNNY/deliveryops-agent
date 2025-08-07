const StatusCard = ({ status }) => (
  <div>
    <h3>Project Status</h3>
    <pre>{JSON.stringify(status, null, 2)}</pre>
  </div>
);
export default StatusCard;
