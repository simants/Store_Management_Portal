import Head from "next/head";
import { Box, Container, Grid } from "@mui/material";
import { Budget } from "../components/dashboard/budget";
import { LatestOrders } from "../components/dashboard/latest-orders";
import { LatestProducts } from "../components/dashboard/latest-products";
import { Sales } from "../components/dashboard/sales";
import { TasksProgress } from "../components/dashboard/tasks-progress";
import { TotalCustomers } from "../components/dashboard/total-customers";
import { TotalProfit } from "../components/dashboard/total-profit";
import { TrafficByDevice } from "../components/dashboard/traffic-by-device";
import { DashboardLayout } from "../components/dashboard-layout";
import { useEffect, useState } from "react";
import axios from "axios";
import { baseUrl } from "src/utils/get-initials";

const Dashboard = () => {
  const [store_id, setStoreId] = useState("");
  const [blockValues, setBlockValues] = useState({});
  const [expenseValues, setExpenseValues] = useState({});
  const [salesValues, setSalesValues] = useState({});

  useEffect(() => {
    getBlockValues();
    getExpenseValues();
    getSalesValues();
  }, []);

  const getBlockValues = (store_id = "all") => {
    setStoreId(store_id);
    axios({
      url: baseUrl + `dashboard_values?store_id=${store_id}`,
      method: "get",
    }).then((res) => {
      console.log(res.data);
      setBlockValues(res.data);
    });
  };

  const getExpenseValues = (store_id = "all") => {
    setStoreId(store_id);
    axios({
      url: baseUrl + `dashboard_expense?store_id=${store_id}`,
      method: "get",
    }).then((res) => {
      console.log(res.data);
      setExpenseValues(res.data);
    });
  };

  const getSalesValues = (store_id = "all", days = 365) => {
    setStoreId(store_id);
    axios({
      url: baseUrl + `dashboard_sales?store_id=${store_id}&days=${days}`,
      method: "get",
    }).then((res) => {
      setSalesValues(res.data);
    });
  };

  const salesParentCallback = (days) => {
    // getSalesValues(store_id, days);
    getSalesValues(store_id);
  };

  return (
    <>
      <Head>
        <title>Dashboard | Material Kit</title>
      </Head>
      <Box
        component="main"
        sx={{
          flexGrow: 1,
          py: 8,
        }}
      >
        <DashboardLayout
          parentCallback={(val) => {
            getBlockValues(val);
            getExpenseValues(val);
            // getSalesValues(val);
          }}
        >
          <Container maxWidth={false}>
            <Grid container spacing={3}>
              <Grid item lg={3} sm={6} xl={3} xs={12}>
                <Budget blockValues={blockValues} />
              </Grid>
              <Grid item xl={3} lg={3} sm={6} xs={12}>
                <TotalCustomers blockValues={blockValues} />
              </Grid>
              <Grid item xl={3} lg={3} sm={6} xs={12}>
                <TasksProgress blockValues={blockValues} />
              </Grid>
              <Grid item xl={3} lg={3} sm={6} xs={12}>
                <TotalProfit blockValues={blockValues} sx={{ height: "100%" }} />
              </Grid>
              <Grid item lg={8} md={12} xl={9} xs={12}>
                <Sales salesValues={salesValues} salesParentCallback={salesParentCallback} />
              </Grid>
              <Grid item lg={4} md={6} xl={3} xs={12}>
                <TrafficByDevice expenseValues={expenseValues} sx={{ height: "100%" }} />
              </Grid>
              <Grid item lg={4} md={6} xl={3} xs={12}>
                <LatestProducts sx={{ height: "100%" }} />
              </Grid>
              <Grid item lg={8} md={12} xl={9} xs={12}>
                <LatestOrders />
              </Grid>
            </Grid>
          </Container>
        </DashboardLayout>
      </Box>
    </>
  );
};

export default Dashboard;
