const Risks = ({ risks }) => (
  <div>
    <h3>Risks</h3>
    <ul>{risks.map((r, i) => <li key={i}>{r}</li>)}</ul>
  </div>
);
export default Risks;
