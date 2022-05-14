import { Container } from "../../styles/global";
import { Table } from "../Table";
import * as S from "./styles";


export function Home() {
    return (
        <Container>
            <S.Wrapper>
                <Table />
            </S.Wrapper>
        </Container>
  )
}