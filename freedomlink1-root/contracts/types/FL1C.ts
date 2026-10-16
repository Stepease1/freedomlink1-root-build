import { Contract } from "ethers";

export enum FL1CRole {
  NONE,
  FOUNDER,
  AGENCY,
  TREASURY,
  EDITORIAL,
  ROOTSTONE,
  GOVERNANCE
}

export interface FL1C extends Contract {
  governanceRouter(): Promise<string>;
  epochAuthority(): Promise<string>;
  rootstoneRegistry(): Promise<string>;
  lineageRegistry(): Promise<string>;
  currentEpoch(): Promise<bigint>;
  lineageNode(): Promise<string>;
  balanceOf(account: string): Promise<bigint>;
  roleOf(account: string): Promise<bigint>;
  mintCredential(to: string, role: FL1CRole, amount: bigint): Promise<void>;
  burnCredential(from: string, amount: bigint): Promise<void>;
  changeRole(account: string, newRole: FL1CRole): Promise<void>;
  bindEpoch(epochId: bigint, newLineageNode: string): Promise<void>;
  transfer(to: string, amount: bigint): Promise<void>;
  transferFrom(from: string, to: string, amount: bigint): Promise<void>;
  approve(spender: string, amount: bigint): Promise<void>;
  allowance(owner: string, spender: string): Promise<bigint>;
}
