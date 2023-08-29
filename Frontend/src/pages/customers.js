import Head from "next/head";
import { Box, Container } from "@mui/material";
import { CustomerListResults } from "../components/customer/customer-list-results";
import { CustomerListToolbar } from "../components/customer/customer-list-toolbar";
import { DashboardLayout } from "../components/dashboard-layout";
import { customers } from "../__mocks__/customers";
import { useState, useEffect } from "react";
import axios from "axios";
import { baseUrl } from "src/utils/get-initials";

const Customers = () => {
  const [params, setParams] = useState();
  const [employeeRatings, setEmployeeRatings] = useState({});
  const [paymentData, setPaymentData] = useState({});
  const [productData, setProductData] = useState({});
  const [lossReportData, setLossReportData] = useState({});
  const [busyHourData, setBusyHourData] = useState({});
  const [store_id, setStoreId] = useState("all");

  useEffect(() => {
    getEmployeeRatings(store_id);
    getPaymentAnalysisData(store_id);
    getProductAnalysisData(store_id);
    getLossReportData(store_id);
    getBusyHourData(store_id);
  }, []);

  const getEmployeeRatings = (store_id = "all") => {
    setStoreId(store_id);
    axios({
      url: baseUrl + `employee_performance_analysis?store_id=${store_id}&year_or_month=month&start_date=2000-01&end_date=2022-12`,
      method: "get",
    }).then((res) => {
      // console.log(res.data);
      setEmployeeRatings(res.data);
    });
  };

  const getPaymentAnalysisData = (store_id = "all") => {
    setStoreId(store_id);
    axios({
      url: baseUrl + `payment_type_report?store_id=${store_id}&year_or_month=month&start_date=2000-01&end_date=2022-12`,
      method: "get",
    }).then((res) => {
      setPaymentData(res.data);
    });
  };

  const getProductAnalysisData = (store_id = "all") => {
    setStoreId(store_id);
    axios({
      url: baseUrl + `brand_local_performance?store_id=${store_id}&year_or_month=month&start_date=2000-01&end_date=2022-12`,
      method: "get",
    }).then((res) => {
      setProductData(res.data);
    });
  };

  const getLossReportData = (store_id = "all") => {
    setStoreId(store_id);
    axios({
      url: baseUrl + `loss_report?store_id=${store_id}&year_or_month=month&start_date=2000-01&end_date=2022-12`,
      method: "get",
    }).then((res) => {
      console.log(res.data);
      setLossReportData(res.data);
    });
  };

  const getBusyHourData = (store_id = "all") => {
    setStoreId(store_id);
    axios({
      url: baseUrl + `busy_hour_analysis?store_id=${store_id}&year_or_month=year&start_date=2021&end_date=2022`,
      method: "get",
    }).then((res) => {
      setBusyHourData(res.data);
    });
  };

  const handleCallback = (val) => {
    setStoreId(val);
    getProductAnalysisData(val);
    getLossReportData(val);
    getBusyHourData(val);
    getEmployeeRatings(val);
    getPaymentAnalysisData(val);
  };

  return (
    <>
      <Head>
        <title>Reports | Material Kit</title>
      </Head>
      <DashboardLayout parentCallback={handleCallback}>
        <Box
          component="main"
          sx={{
            flexGrow: 1,
            py: 8,
          }}
        >
          <Container maxWidth={false}>
            <CustomerListToolbar parentCallBack={setParams} />
            <Box sx={{ mt: 3 }}>
              <CustomerListResults
                employeeRatings={employeeRatings}
                paymentData={paymentData}
                productData={productData}
                lossReportData={lossReportData}
                busyHourData={busyHourData}
                params={params}
              />
            </Box>
          </Container>
        </Box>
      </DashboardLayout>
    </>
  );
};

export default Customers;
