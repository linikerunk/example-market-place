import { Button } from "../Button";
import { Input } from "../Input";
import { FaTrash } from "react-icons/fa";
import { Flex } from "../Vendas/styles";
import * as S from "./style";
import { useEffect, useState } from "react";
import { API } from "../../services/api";

export function Table({ setIsOpen }) {
  const [data, setData] = useState([]);
  async function getData() {
    const response = await API.get("product_activitys/");
    setData(response.data);
  }
  useEffect(() => {
    getData();
  }, []);

  async function handleRemoveProduct(props) {
    const response = await API.delete(`product_activitys/${props}/`)
    await getData();
  }

  return (
    <S.Container data-aos="fade-right">
      <S.TitlePag>Produtos</S.TitlePag>
      <Flex>
        <Input
          widthInput={"30rem"}
          type={"text"}
          setData={setData}
          text={"Buscar pelo código de barras ou descição"}
        />
        <Input
          type={"number"}
          widthInput={"15rem"}
          min={0}
          text={"Quantidade de itens"}
        />
        <Button color={"#1137f1ed"} click={() => setIsOpen(true)}>Adicionar</Button>
      </Flex>
      <S.Table>
        <S.Columns>
          <S.Title widthTitle={"7rem"}>Id</S.Title>
          <S.Title widthTitle="25rem">Produto/Serviço</S.Title>
          <S.Title widthTitle="15rem">Quantidade</S.Title>
          <S.Title widthTitle="15rem">Preço unitário</S.Title>
          <S.Title widthTitle="10rem">Total</S.Title>
        </S.Columns>

        {data.map(({ name, pk, price, quantity, _get_total_price }) => (
          <S.Columns>
            <S.Items>{pk}</S.Items>
            <S.Items>{name}</S.Items>
            <S.Items>{quantity}</S.Items>
            <S.Items>{price}</S.Items>
            <S.Items>{_get_total_price}</S.Items>
            <S.Items>
              <FaTrash onClick={() => handleRemoveProduct(pk)} />
            </S.Items>
          </S.Columns>
        ))}
      </S.Table>
    </S.Container>
  );
}
