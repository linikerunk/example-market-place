import { Container } from "../../styles/global";
import { Table } from "../Table";
import { Vendas } from "../Vendas";

import * as S from "./styles";

export function Home() {
    return (
        <Container>
        <S.Wrapper>
            <Table />
            <Vendas />
        </S.Wrapper>
    </Container>
  )
}