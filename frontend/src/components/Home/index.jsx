import { Container } from "../../styles/global";
import { Vendas } from "../Vendas";
import { Table } from "../Table";
import { Modal } from "../Modal";
import { Button } from "../Button";

import { useState } from "react";

import * as S from "./styles";

export function Home() {
  const [status, setStatus] = useState(false);
  
  return (
    <>
      <Container>
        <S.Wrapper>
          <Table setIsOpen={setStatus} />
          <Vendas />
        { status && <Modal isExit={status} setIsExit={setStatus} />}
        </S.Wrapper>
      </Container>
    </>
  );
}
