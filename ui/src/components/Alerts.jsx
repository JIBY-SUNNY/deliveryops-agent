const Alerts = ({ alerts }) => (
  <div>
    <h3>Alerts</h3>
    <ul>{alerts.map((a, i) => <li key={i}>{a}</li>)}</ul>
  </div>
);
export default Alerts;
