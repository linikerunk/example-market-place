import { Button } from "../Button";
import { useState, useEffect } from 'react'
import { API } from '../../services/api'
import { TitlePag } from "../Table/style";
import * as S from "./styles";

export function Vendas() {
  const [sellers, setSellers] = useState([])
  const [clients, setClients] = useState([])

  async function getData() {
    const response = await API.get("sellers/");
    const { data } = await API.get('clients/')
    setSellers(response.data)
    setClients(data)
  }
  useEffect(() => {
    getData();
  }, []);

  return (
    <>
      <S.Wrapper>
        <TitlePag data-aos="fade-down">Dados da venda</TitlePag>
        <S.Box data-aos="fade-left">
          <S.Items>
            <S.Label>Escolha um vendedor</S.Label>
            <S.Select>
              {sellers.map(({ name, id }) => (
                <option>{name}</option>
              ))}
            </S.Select>
          </S.Items>
          <S.Items>
            <S.Label>Escolha um cliente</S.Label>
            <S.Select>
              {clients.map(({ name, id }) => (
                <option key={id} value={id}>{ name }</option>
              ))}
            </S.Select>
          </S.Items>
        </S.Box>

        <S.Footer>
          <S.Flex>
            <S.PriceTotal>Valor total de venda</S.PriceTotal>
            <S.Price>R$ 146,10</S.Price>
          </S.Flex>
          <S.Flex>
            <Button color={"#1137f1ed"}>Cancelar</Button>
            <Button color={"#049237"}>Finalizar</Button>
          </S.Flex>
        </S.Footer>
      </S.Wrapper>
    </>
  );
}
