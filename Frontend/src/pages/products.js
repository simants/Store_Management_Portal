import Head from "next/head";
import { Box, Container, Grid, Pagination } from "@mui/material";
import { products } from "../__mocks__/products";
import { ProductListToolbar } from "../components/product/product-list-toolbar";
import { ProductCard } from "../components/product/product-card";
import { DashboardLayout } from "../components/dashboard-layout";
import { useEffect, useState } from "react";
import axios from "axios";
import { baseUrl } from "src/utils/get-initials";

const Products = () => {
  const [productvalues, setProductValues] = useState({});
  const [store_id, setStoreId] = useState("all");

  useEffect(() => {
    getProductValues(store_id);
  }, []);

  const getProductValues = (store_id) => {
    setStoreId(store_id);
    axios({
      url: baseUrl + `products?store_id=${store_id}&search=0`,
      method: "get",
    }).then((res) => {
      console.log(res.data.data);
      setProductValues(res.data.data);
    });
  };

  const searchParentCallback = (val) => {
    axios({
      url: baseUrl + `products?store_id=${store_id}&search=${val}`,
      method: "get",
    }).then((res) => {
      console.log(res.data.data);
      setProductValues(res.data.data);
    });
  }

  const handleParentCallback = (val) => {
    setStoreId(val)
    getProductValues(val)
  }

  return (
    <>
      <Head>
        <title>Products | Material Kit</title>
      </Head>

      <Box
        component="main"
        sx={{
          flexGrow: 1,
          py: 8,
        }}
      >
        <DashboardLayout parentCallback={handleParentCallback}>
          <Container maxWidth={false}>
            <ProductListToolbar />
            <ProductCard
              productvalues={productvalues}
              productParentCallback={getProductValues}
              searchParentCallback={searchParentCallback}
            />
          </Container>
        </DashboardLayout>
      </Box>
    </>
  );
};

export default Products;
