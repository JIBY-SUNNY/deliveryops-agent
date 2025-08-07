import { useEffect, useState } from 'react';
import { runAgent } from '../api/api';
import StatusCard from '../components/StatusCard';
import Risks from '../components/Risks';
import Alerts from '../components/Alerts';

const Dashboard = () => {
  const [data, setData] = useState({ project_status: {}, risks: [], alerts: [] });

  useEffect(() => {
    runAgent().then(setData).catch(console.error);
  }, []);

  return (
    <div>
      <h1>DeliveryOps Dashboard</h1>
      <StatusCard status={data.project_status} />
      <Risks risks={data.risks} />
      <Alerts alerts={data.alerts} />
    </div>
  );
};

export default Dashboard;
