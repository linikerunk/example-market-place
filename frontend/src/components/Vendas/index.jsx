import { Button } from "../Button";
import { TitlePag } from "../Table/style";
import * as S from "./styles";

export function Vendas() {
  return (
    <>
      <S.Wrapper>
        <TitlePag data-aos="fade-down">Dados da venda</TitlePag>
        <S.Box data-aos="fade-left">
          <S.Items>
            <S.Label>Escolha um vendedor</S.Label>
            <S.Select>
              <option selected="">Selecione o nome</option>
              <option value="1">One</option>
              <option value="2">Two</option>
              <option value="3">Three</option>
            </S.Select>
          </S.Items>
          <S.Items>
            <S.Label>Escolha um cliente</S.Label>
            <S.Select>
              <option selected="">Selecione o nome</option>
              <option value="1">One</option>
              <option value="2">Two</option>
              <option value="3">Three</option>
            </S.Select>
          </S.Items>
        </S.Box>

        <S.Footer>
          <S.Flex>
            <S.PriceTotal>Valor total de venda</S.PriceTotal>
            <S.Price>R$ 146,10</S.Price>
          </S.Flex>
          <S.Flex>
            <Button color={"#E92929"}>Cancelar</Button>
            <Button color={"#049237"}>Finalizar</Button>
          </S.Flex>
        </S.Footer>
      </S.Wrapper>
    </>
  );
}
