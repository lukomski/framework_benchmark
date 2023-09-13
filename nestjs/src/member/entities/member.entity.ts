import { Column, Entity, PrimaryGeneratedColumn } from 'typeorm';

@Entity()
export class Member {
  @PrimaryGeneratedColumn({
    type: 'bigint',
    name: 'member_id',
  })
  id: number;

  @Column({
    nullable: false,
    default: '',
  })
  name: string;
}
