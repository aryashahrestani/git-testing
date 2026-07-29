import type { GetStaticPropsContext, NextPage } from "next";
import Head from "next/head";
import HomePage from "../../components/PagesComponents/HomePage";
import axios from "axios";
import {
  AttributesValueModel,
  breadcrumbItem,
  category_item,
  ColorItem,
  ProductCombinationModel,
  ProductMediaModel,
  ProductSummaryModel,
} from "../../context/_models";
import {
  backToFrontModel_category,
  backToFrontModel_productSummery,
} from "../../Helper";
import { receiveCategories } from "../../Services/shopCategoryServer";
import SparePartsLandingPageComponent from "../../components/PagesComponents/SparePartsLanding";
import { getProducts } from "../../Services/productServer";
import { useRouter } from "next/router";
import { getHeadTags } from "../../Helper/seo_helper";
type props = {
  categories: category_item[];
  special_Sale_Items: ProductSummaryModel[];
  most_selling_products: ProductSummaryModel[];
  rare_products: ProductSummaryModel[];
  discounted_products: ProductSummaryModel[];
  first_slider_products: ProductSummaryModel[];
};
const SparePartsLanding: NextPage<props> = (props: props) => {
  const { pathname } = useRouter();
  let seo = getHeadTags({ pathname });
  const {
    categories,
    special_Sale_Items,
    most_selling_products,
    rare_products,
    discounted_products,
    first_slider_products,
  } = props;
  return (
    <>
      <Head>
        <title>{seo.title}</title>
        {seo?.metaKeywords ? (
          <meta name="keywords" content={seo.metaKeywords} />
        ) : null}
        {seo?.metaDescription ? (
          <meta name="description" content={seo.metaDescription} />
        ) : null}
      </Head>
      <SparePartsLandingPageComponent
        categories={categories}
        suggested_Items1={most_selling_products}
        suggested_Items2={rare_products}
        discounted_products={discounted_products}
        first_slider_products={first_slider_products}
      ></SparePartsLandingPageComponent>
    </>
  );
};

export async function getStaticProps(context: GetStaticPropsContext) {
  const isFirstTime = context.previewData === undefined; //is at build time
  let categories = [] as category_item[];
  let most_selling_products = [] as ProductSummaryModel[];
  let rare_products = [] as ProductSummaryModel[];
  let discounted_products = [] as ProductSummaryModel[];
  //first slider starts
  let first_slider_products = [] as ProductSummaryModel[];
  let lcd_products = [] as ProductSummaryModel[];
  let battery_products = [] as ProductSummaryModel[];
  let flat_products = [] as ProductSummaryModel[];
  let door_products = [] as ProductSummaryModel[];
  //first slider ends

  let success = false;
  let attempts_count = 0;
  let attempts_count_to_break = 5;
  while (!success && attempts_count < attempts_count_to_break) {
    try {
      discounted_products = await getProducts({
        categoryId: [18],
        discountedProducts: "True",
      });
      lcd_products = await getProducts({
        categoryId: [54],
      });
      battery_products = await getProducts({
        categoryId: [55],
      });
      flat_products = await getProducts({
        categoryId: [56],
      });
      door_products = await getProducts({
        categoryId: [61],
      });

      //categories
      const categories_resp = (await receiveCategories()) as category_item[];
      let Qataat_id = categories_resp.find(
        (item) => item.title === "قطعات"
      )?.id;
      if (Qataat_id != null)
        categories = categories_resp.filter(
          (item) => item.parent_id === Qataat_id
        );
      //most_selling_products
      const suggested_Items1_resp = await axios.get(
        process.env.BACKENDURL +
          "/shop/admin/product_api/?order=2&categoryId=18"
      );
      if (suggested_Items1_resp.data.products) {
        const suggested_Items1_backModels = suggested_Items1_resp.data.products;
        const suggested_Items1_frontModels = suggested_Items1_backModels.map(
          (item: any) => backToFrontModel_productSummery(item)
        );
        most_selling_products = suggested_Items1_frontModels;
      }
      //rare_products
      const suggested_Items2_resp = await axios.get(
        process.env.BACKENDURL +
          "/shop/admin/product_api/?tagId=11&categoryId=18" //11 is kamyab
      );
      if (suggested_Items2_resp.data.products) {
        const suggested_Items2_backModels = suggested_Items2_resp.data.products;
        const suggested_Items2_frontModels = suggested_Items2_backModels.map(
          (item: any) => backToFrontModel_productSummery(item)
        );
        rare_products = suggested_Items2_frontModels;
      }
      first_slider_products = [
        ...lcd_products,
        ...battery_products,
        ...flat_products,
        ...door_products,
      ];
      success = true;
    } catch (error: any) {
      if (
        error &&
        error.response &&
        error.response.status &&
        error.response.status === 404
      ) {
        attempts_count = attempts_count_to_break;
      } else {
        attempts_count = attempts_count + 1;
      }
    }
  }
  if (!success && !isFirstTime) {
    throw new Error("Not revalidated");
  }
  return {
    props: {
      categories: categories,
      most_selling_products: most_selling_products,
      rare_products: rare_products,
      discounted_products,
      first_slider_products,
    }, // will be passed to the page component as props
    revalidate: 5,
  };
}
export default SparePartsLanding;
