package escoladeconducao;

import myinputs.*;
import java.io.*;
import java.util.*;


public class EscolaDeConducao {
    public static void main(String[] args) throws IOException {
        int menu, cat, dia;
        boolean k = false, bo=false, b;
        Horario h = new Horario();
        
        Aluno a = new Aluno("");
        Professor p = new Professor("");
        ArrayList<Aluno> listaA = new ArrayList<Aluno>();
        ArrayList<Professor> listaP = new ArrayList<Professor>();
        
        try {
            ObjectInputStream is = new ObjectInputStream(new FileInputStream("dataBaseA.dat"));
            
            int ult = is.readInt();
            a.setUlt(ult);
            
            listaA = (ArrayList<Aluno>)is.readObject();
        }
        catch (IOException e){
            System.out.println(e.getMessage());
        }
        catch(ClassNotFoundException e) {
            System.out.println(e.getMessage());
        }
        
        try {
            ObjectInputStream is = new ObjectInputStream(new FileInputStream("dataBaseP.dat"));
            
            int ult = is.readInt();
            p.setUlt(ult);
            listaP = (ArrayList<Professor>)is.readObject();
        }
        catch (IOException e){
            System.out.println(e.getMessage());
        }
        catch(ClassNotFoundException e) {
            System.out.println(e.getMessage());
        }
        
        while(true) {
            System.out.println("\n---MENU---");
            System.out.println("1) Criar Utilizador");
            System.out.println("2) Consultar Utilizador");
            System.out.println("3) Alterar Utilizador");
            System.out.println("4) Eliminar Utilizador");
            System.out.println("0) Sair");
            System.out.print("Menu: ");
            menu = Ler.umInt();
            
            switch(menu) {
                case 0: //Sair
                    
                    //Guardar Alunos no ficheiro
                    try {
                        ObjectOutputStream os = new ObjectOutputStream (new FileOutputStream("dataBaseA.dat"));
                        
                        os.writeInt(a.getUlt());
                        os.writeObject(listaA);
                        
                        os.flush();
                    }
                    catch (IOException e){
                        System.out.println(e.getMessage());
                    }
                    
                    //Guardar Professores no ficheiro
                    try {
                        ObjectOutputStream os = new ObjectOutputStream (new FileOutputStream("dataBaseP.dat"));
                
                        os.writeInt(p.getUlt());
                        os.writeObject(listaP);
                
                        os.flush();
                    }
                    catch (IOException e){
                        System.out.println(e.getMessage());
                    }
                    
                    
                    System.out.println("\nTrabalho realizado por: ");
                    System.out.println("Alexandre Antão, nº 37416");
                    System.out.println("Tomás Jerónimo, nº 37870");
                    System.out.println("João Brito, nº 37880");
                    System.out.println("Ricardo Domingos, nº 37906");
                    
                    System.exit(0);
                    
                case 1: //Criar Utilizador
                    k = false;
                    while(k==false) {
                        System.out.println("\n---CRIAR UTILIZADOR---");
                        System.out.println("1) Criar Aluno");
                        System.out.println("2) Criar Professor");
                        System.out.println("0) Voltar");
                        System.out.print("Menu: ");
                        menu = Ler.umInt();
                            
                        switch(menu) {
                            case 0: //Voltar
                                k=true;
                                break;
                            case 1: //Criar Aluno
                                if(listaP.size()==0) {
                                    System.out.println("\nNão existem Professores disponiveis \n");
                                    break;
                                }
                                
                                System.out.print("Introduza o nome: ");
                                String nome = Ler.umaString();
                                
                                System.out.println("Categorias: ");
                                System.out.println("1) Categoria A (Motociclos)");
                                System.out.println("2) Categoria B (Ligeiros)");
                                System.out.println("3) Cateria A+B (Motociclos + Ligeiros)");
                                System.out.println("4) Categoria C (Pesados de Mercadorias)");
                                System.out.println("5) Categoria D (Pesados de Passageiros)");
                                System.out.print("Categoria: ");
                                cat = Ler.umInt();
                                while(cat<1 || cat>5) {
                                    System.out.print("Opção inválida. Escolha uma opção valida: ");
                                    cat = Ler.umInt();
                                }
                                
                                System.out.println("\nHorario: ");
                                System.out.println("1) Segunda-feira");
                                System.out.println("2) Terça-feira");
                                System.out.println("3) Quarta-feira");
                                System.out.println("4) Quinta-feira");
                                System.out.println("5) Sexta-feira");
                                System.out.print("Dia: ");
                                dia = Ler.umInt();
                                
                                do {
                                    while(dia<1 || dia>5) {
                                        System.out.print("Opção Inválida. Escolha uma opção válida: ");
                                        dia = Ler.umInt();
                                    }
                                    for(int i=0;i<listaP.size();i++){
                                        if( bo=listaP.get(i).existeDia(listaP.get(i).getHorario(), dia)==true)
                                            break;
                                    }
                                    if(bo == false) {
                                        System.out.print("Não há horários disponiveis neste dia. \nIntroduza uma nova opção: ");
                                        dia = Ler.umInt();
                                    }
                                }while(bo!=true);
                                boolean n;
                                int op1=0, op2=0, op3=0;
                                for(int i=0;i<listaP.size();i++) {
                                    if( bo=listaP.get(i).existeDia(listaP.get(i).getHorario(), dia)==true) {
                                        //Imprimir horarios dos Professores
                                        op1++;
                                        System.out.println("\n" + op1 +") Professor: " + listaP.get(i).getNome() + "\nHorários disponiveis: ");
                                        for(int j=0;j<listaP.get(i).horario.size();j++) {
                                            if(listaP.get(i).horario.get(j).getDia()==dia)
                                            System.out.println("\t" + listaP.get(i).horario.get(j).getHora() + "h - " + ( listaP.get(i).horario.get(j).getHora()+2 ) + "h | " + listaP.get(i).horario.get(j).getTipoAula());
                                        }
                                    }    
                                            
                                }
                                
                                System.out.print("Professor: ");
                                int opProf = Ler.umInt();
                                while(opProf<=0 || opProf>op1) {
                                    System.out.print("Opção Inválida. Escolha uma opção válida: ");
                                    opProf = Ler.umInt();
                                }
                                
                                for(int i=0;i<listaP.size();i++) {
                                    if( bo=listaP.get(i).existeDia(listaP.get(i).getHorario(), dia)==true) {
                                        op2++; 
                                        if(opProf == op2) {
                                            for(int j=0;j<listaP.get(i).horario.size();j++) {
                                                if(listaP.get(i).horario.get(j).getDia()==dia) {
                                                    op3++;
                                                    System.out.println("\t" + op3 + ") " + listaP.get(i).horario.get(j).getHora() + "h - " + ( listaP.get(i).horario.get(j).getHora()+2 ) + "h | " + listaP.get(i).horario.get(j).getTipoAula());
                                                    
                                                }
                                            }
                                            System.out.print("Menu: ");
                                            int opHoras = Ler.umInt();
                                            while(opHoras<=0 || opHoras>op3) {
                                                System.out.print("Opção Inválida. Escolha uma opção válida: ");
                                                opHoras = Ler.umInt();
                                            }
                                            op3=0;
                                            for(int j=0;j<listaP.get(i).horario.size();j++) {
                                                if(listaP.get(i).horario.get(j).getDia()==dia) {
                                                    op3++;
                                                    if(op3==opHoras)
                                                        h.setHora(listaP.get(i).horario.get(j).getHora());
                                                        h.setnomeP(listaP.get(i).getNome());
                                                        h.setDia(listaP.get(i).horario.get(j).getDia());
                                                        h.setTipoAula(listaP.get(i).horario.get(j).getTipoAula());
                                                }
                                            }
                                            
                                        }
                                    }
                                }
                                
                                
                                Aluno alu = new Aluno(nome);
                                alu.setCategoria(cat);
                                alu.addHorario((Horario)h.clone());
                                
                                listaA.add(alu);
                                
                                break;
                                
                            case 2: //Criar Professor
                                System.out.print("Introduza o nome: ");
                                nome = Ler.umaString();
                                
                                System.out.print("Salario: ");
                                float salario = Ler.umFloat();
                                Professor prof = new Professor(nome, salario);
                                k = false;
                                do {
                                    System.out.println("\nHorario: ");
                                    System.out.println("1) Segunda-feira");
                                    System.out.println("2) Terça-feira");
                                    System.out.println("3) Quarta-feira");
                                    System.out.println("4) Quinta-feira");
                                    System.out.println("5) Sexta-feira");
                                    System.out.print("Dia: ");
                                    dia = Ler.umInt();
                                    while(dia<1 || dia>5) {
                                        System.out.print("Opção Inválida. Escolha uma opção válida: ");
                                        dia = Ler.umInt();
                                    }
                                    int hora=prof.mostrarHorarioDisponivel(dia);
                                    if(hora == 0) {
                                        System.out.println("\nNão há mais horários disponiveis neste dia");
                                        continue;
                                    }
                                    System.out.println("Tipo de aula: ");
                                    System.out.println("1) Condução");
                                    System.out.println("2) Código");
                                    System.out.print("Menu: ");
                                    int tipo = Ler.umInt();
                                    while(tipo < 1 || tipo > 2) {
                                        System.out.print("Opção Inválida. Escolha uma opção válida: ");
                                        tipo = Ler.umInt();
                                    }
                                    
                                    if(tipo == 1)
                                        h.setTipoAula("Condução");
                                    else
                                        h.setTipoAula("Código");
                                    h.setHora(hora);
                                    h.setDia(dia);
                                    h.setnomeP(nome);
                                    
                                    prof.addHorario((Horario)h.clone());
                                    System.out.print("Adicionar outro horário? (S/N): ");
                                    char r = Ler.umChar();
                                    while(r != 's' && r != 'S' && r != 'n' && r != 'N') {
                                        System.out.print("Opção Inválida. Escolha uma opção válida: ");
                                        r = Ler.umChar();
                                    }
                                    if(r == 's' || r == 'S')
                                        continue;
                                    else
                                        k = true;
                                    
                                }while(k!=true);
                                
                                listaP.add(prof);
                                
                                break;
                        }
                        
                    }
                break;
                
                case 2: //Consultar Utilizador
                    k = false;
                    do {
                        System.out.println("");
                        System.out.println("---CONSULTAR UTILIZADOR---");
                        System.out.println("1) Consultar Aluno");
                        System.out.println("2) Consultar Professor");
                        System.out.println("3) Listar");
                        System.out.println("0) Voltar");
                        System.out.print("Menu: ");
                        menu = Ler.umInt();
                        while(menu < 0 || menu > 3) {
                            System.out.print("Opção Inválida. Escolha uma opção válida: ");
                            menu = Ler.umInt();
                        }
                        
                        int num;
                        
                        switch(menu) {
                            case 0:  //Voltar
                                k = true;
                                break;
                            case 1: //Consultar Aluno
                                do {
                                    System.out.print("Indique o Numero de identificação: ");
                                    num = Ler.umInt();
                                    //Corrigir numero
                                    b=false;
                                    for(int i=0;i<listaA.size();i++){
                                        if(listaA.get(i).getNumero()==num){
                                            num=i+1;
                                            b=true;
                                            break;
                                        }
                                    }
                                    if(b==false){
                                        System.out.println("\nNão existe um aluno com este número");

                                    }
                                }while(b!=true);
                                
                                System.out.println("\nNome: " + listaA.get(num-1).getNome() + " | " + "Categoria: " + listaA.get(num-1).getCategoria());
                                
                                for(int j=0;j<listaA.get(num-1).horario.size();j++) {
                                    System.out.println("\t" + listaA.get(num-1).horario.get(j).imprimeDia() + ": " + listaA.get(num-1).horario.get(j).getHora() + "h - " + (listaA.get(num-1).horario.get(j).getHora()+2) + "h | " + listaA.get(num-1).horario.get(j).getTipoAula() + " | Professor: " + listaA.get(num-1).horario.get(j).getnomeP());
                                }
                                break;
                            case 2: //Consultar Professor
                                do {
                                    System.out.print("Indique o Numero de identificação: ");
                                    num = Ler.umInt();
                                    //Corrigir numero
                                    b=false;
                                    for(int i=0;i<listaP.size();i++){
                                        if(listaP.get(i).getNumero()==num){
                                            num=i+1;
                                            b=true;
                                            break;
                                        }
                                    }
                                    if(b==false){
                                        System.out.println("\nNão existe um aluno com este número");

                                    }
                                }while(b!=true);
                                
                                System.out.println("\nNome: " + listaP.get(num-1).getNome() + " | " + "Salario: " + listaP.get(num-1).getSalario());
                                
                                for(int j=0;j<listaP.get(num-1).horario.size();j++) {
                                        System.out.println("\t" + listaP.get(num-1).horario.get(j).imprimeDia() + ": " + listaP.get(num-1).horario.get(j).getHora() + "h - " + (listaP.get(num-1).horario.get(j).getHora()+2) + "h | " + listaP.get(num-1).horario.get(j).getTipoAula());
                                    }
                                
                                break;
                            case 3: //Listar Alunos e Professores
                                System.out.println("\n---LISTA ALUNOS--- ");
                                for(int i=0;i<listaA.size();i++) {
                                    System.out.println("Numero: " + listaA.get(i).getNumero() + " | Nome: " + listaA.get(i).getNome() + " | Categoria: " + listaA.get(i).getCategoria());
                                    for(int j=0;j<listaA.get(i).horario.size();j++) {
                                        System.out.println("\t" + listaA.get(i).horario.get(j).imprimeDia() + ": " + listaA.get(i).horario.get(j).getHora() + "h - " + (listaA.get(i).horario.get(j).getHora()+2) + "h | " + listaA.get(i).horario.get(j).getTipoAula() + " | Professor: " + listaA.get(i).horario.get(j).getnomeP());
                                    }
                                }
                                System.out.println("\n---LISTA PROFESSORES---");
                                for(int i=0;i<listaP.size();i++) {
                                    System.out.println("Numero: " + listaP.get(i).getNumero() + " | Nome: " + listaP.get(i).getNome() + " | Salario: " + listaP.get(i).getSalario());
                                    for(int j=0;j<listaP.get(i).horario.size();j++) {
                                        System.out.println("\t" + listaP.get(i).horario.get(j).imprimeDia() + ": " + listaP.get(i).horario.get(j).getHora() + "h - " + (listaP.get(i).horario.get(j).getHora()+2) + "h | " + listaP.get(i).horario.get(j).getTipoAula());
                                    }
                                }
                                
                                break;
                        }
                    }while(k!=true);
                    
                    break;
                case 3: //Alterar Utilizadores
                    k = false;
                    String nome;
                    int num;
                    do {
                        System.out.println("\n---ALTERAR UTILIZADOR---");
                        System.out.println("1) Alterar informação de Alunos");
                        System.out.println("2) Alterar informação de Professores");
                        System.out.println("0) Voltar");
                        System.out.print("Menu: ");
                        menu = Ler.umInt();
                        while(menu < 0 || menu > 2) {
                            System.out.print("Opção Inválida. Escolha uma opção válida: ");
                            menu = Ler.umInt();
                        }
                        
                        switch(menu) {
                            case 0: //Voltar
                                k = true;
                                
                                break;
                            case 1: //Alterar Aluno
                                do {
                                    System.out.print("Numero do Aluno a alterar: ");
                                    num = Ler.umInt();
                                    //Corrigir numero
                                    b=false;
                                    for(int i=0;i<listaA.size();i++){
                                        if(listaA.get(i).getNumero()==num){
                                            num=i+1;
                                            b=true;
                                            break;
                                        }
                                    }
                                    if(b==false){
                                        System.out.println("\nNão existe um aluno com este número");

                                    }
                                }while(b!=true);
                                
                                k = false;
                                do {
                                    System.out.println("\n---ALTERAR ALUNO---");
                                    System.out.println("1) Alterar Nome");
                                    System.out.println("2) Alterar Categoria");
                                    System.out.println("3) Alterar Horario");
                                    System.out.println("0) Voltar");
                                    System.out.print("Menu: ");
                                    menu = Ler.umInt();
                                    
                                    switch(menu) {
                                        case 0: //Voltar
                                            k = true;
                                            break;
                                        case 1: //Alterar nome Aluno
                                            System.out.println("\nNome atual: " + listaA.get(num-1).getNome());
                                            System.out.print("Novo nome: ");
                                            nome = Ler.umaString();
                                            listaA.get(num-1).setNome(nome);
                                            
                                            break;
                                        case 2: //Alterar Categoria Aluno
                                            System.out.println("\nCategoria atual: " + listaA.get(num-1).getCategoria());
                                            System.out.println("\nCategorias: ");
                                            System.out.println("1) Categoria A (Motociclos)");
                                            System.out.println("2) Categoria B (Ligeiros)");
                                            System.out.println("3) Cateria A+B (Motociclos + Ligeiros)");
                                            System.out.println("4) Categoria C (Pesados de Mercadorias)");
                                            System.out.println("5) Categoria D (Pesados de Passageiros)");
                                            System.out.print("Nova Categoria: ");
                                            cat = Ler.umInt();
                                            while(cat<1 || cat>5) {
                                                System.out.print("Categoria Inexistente. Indique uma categoria valida: ");
                                                cat = Ler.umInt();
                                            }
                                            listaA.get(num-1).setCategoria(cat);
                                            
                                            break;
                                        case 3: //Alterar Horario Aluno
                                            System.out.println("\n1) Novo Horario");
                                            System.out.println("2) Apagar Horario");
                                            System.out.print("Menu: ");
                                            menu = Ler.umInt();
                                            while(menu<1 || menu>2) {
                                                System.out.print("Opção Inválida. Indique uma nova opção: ");
                                                menu = Ler.umInt();
                                            }
                                                    
                                            if(menu == 1) {
                                                if(listaP.size() == 0) {
                                                    System.out.println("\nNão existem Professores disponíveis");
                                                    break;
                                                }
                                                System.out.println("\nHorario: ");
                                                System.out.println("1) Segunda-feira");
                                                System.out.println("2) Terça-feira");
                                                System.out.println("3) Quarta-feira");
                                                System.out.println("4) Quinta-feira");
                                                System.out.println("5) Sexta-feira");
                                                System.out.print("Dia: ");
                                                dia = Ler.umInt();

                                                do {
                                                    while(dia<1 || dia>5) {
                                                        System.out.print("Opção Inválida. Escolha uma opção válida: ");
                                                        dia = Ler.umInt();
                                                    }
                                                    for(int i=0;i<listaP.size();i++){
                                                        if(bo=listaP.get(i).existeDia(listaP.get(i).getHorario(), dia)==true)
                                                            break;
                                                    }
                                                    if(bo == false) {
                                                        System.out.println("Não há horários disponiveis neste dia. \nIntroduza uma nova opção: ");
                                                        dia = Ler.umInt();
                                                    }
                                                }while(bo!=true);
                                                boolean n;
                                                int op1=0, op2=0, op3=0;
                                                for(int i=0;i<listaP.size();i++) {
                                                    if( bo=listaP.get(i).existeDia(listaP.get(i).getHorario(), dia)==true) {
                                                        //Imprimir horarios dos Professores
                                                        op1++;
                                                        System.out.println("\n" + op1 +") Professor: " + listaP.get(i).getNome() + "\nHorários disponiveis: ");
                                                        for(int j=0;j<listaP.get(i).horario.size();j++) {
                                                            if(listaP.get(i).horario.get(j).getDia()==dia)
                                                            System.out.println("\t" + listaP.get(i).horario.get(j).getHora() + "h - " + ( listaP.get(i).horario.get(j).getHora()+2 ) + "h");
                                                        }
                                                    }    

                                                }

                                                System.out.print("Professor: ");
                                                int opProf = Ler.umInt();
                                                while(opProf<=0 || opProf>op1) {
                                                    System.out.print("Opção Inválida. Escolha uma opção válida: ");
                                                    opProf = Ler.umInt();
                                                }

                                                for(int i=0;i<listaP.size();i++) {
                                                    if( bo=listaP.get(i).existeDia(listaP.get(i).getHorario(), dia)==true) {
                                                        op2++; 
                                                        if(opProf == op2) {
                                                            for(int j=0;j<listaP.get(i).horario.size();j++) {
                                                                if(listaP.get(i).horario.get(j).getDia()==dia) {
                                                                    op3++;
                                                                    System.out.println("\t" + op3 + ") " + listaP.get(i).horario.get(j).getHora() + "h - " + ( listaP.get(i).horario.get(j).getHora()+2 ) + "h");

                                                                }
                                                            }
                                                            System.out.print("Menu: ");
                                                            int opHoras = Ler.umInt();
                                                            while(opHoras<=0 || opHoras>op3) {
                                                                System.out.print("Opção Inválida. Escolha uma opção válida: ");
                                                                opHoras = Ler.umInt();
                                                            }
                                                            op3=0;
                                                            for(int j=0;j<listaP.get(i).horario.size();j++) {
                                                                if(listaP.get(i).horario.get(j).getDia()==dia) {
                                                                    op3++;
                                                                    if(op3==opHoras)
                                                                        h.setHora(listaP.get(i).horario.get(j).getHora());
                                                                        h.setnomeP(listaP.get(i).getNome());
                                                                        h.setDia(listaP.get(i).horario.get(j).getDia());
                                                                        h.setTipoAula(listaP.get(i).horario.get(j).getTipoAula());
                                                                }
                                                            }

                                                        }
                                                    }
                                                }
                                                listaA.get(num-1).addHorario((Horario)h.clone());
                                            }
                                            else {  //Apagar Horario aluno
                                                if(listaA.get(num-1).horario.size() <= 1) {
                                                    System.out.println("\nPrecisa de ter pelo menos um horário");
                                                    break;
                                                }
                                                for(int i=0;i<listaA.get(num-1).horario.size();i++) {
                                                    System.out.println(i+1 + ") " + listaA.get(num-1).horario.get(i).imprimeDia() + ": " + listaA.get(num-1).horario.get(i).getHora() + "h - " + (listaA.get(num-1).horario.get(i).getHora()+2) + listaA.get(num-1).horario.get(i).getTipoAula());
                                                }
                                                System.out.print("Menu: ");
                                                menu = Ler.umInt();
                                                while(menu<=0 || menu>listaA.get(num-1).horario.size()) {
                                                    System.out.print("Opção Inválida. Indique uma nova opção: ");
                                                    menu = Ler.umInt();
                                                }
                                                listaA.get(num-1).horario.remove(menu-1);
                                                
                                            }
                                    break;
                                    }
                                }while(k != true);
                                break;
                            case 2: //Alterar Professor
                                do {
                                    System.out.print("Numero do Professor a alterar: ");
                                    num = Ler.umInt();
                                    //Corrigir numero
                                    for(int i=0;i<listaP.size();i++){
                                        if(listaP.get(i).getNumero()==num){
                                            num=i+1;
                                            break;
                                        }
                                    }
                                }while(num<0 || num>listaP.size());
                                
                                k = false;
                                do {
                                    System.out.println("\n---ALTERAR PROFESSOR---");
                                    System.out.println("1) Alterar Nome");
                                    System.out.println("2) Alterar Salario");
                                    System.out.println("3) Alterar Horario");
                                    System.out.println("0) Voltar");
                                    System.out.print("Menu: ");
                                    menu = Ler.umInt();
                                    while(menu < 0 || menu > 3) {
                                        System.out.print("Opção Inválida. Escolha uma opção válida: ");
                                        menu = Ler.umInt();
                                    }
                                    
                                    switch(menu) {
                                        case 0: //Voltar
                                            k = true;
                                            
                                            break;
                                        case 1: //Alterar Nome Professor
                                            System.out.println("Nome atual: " + listaP.get(num-1).getNome());
                                            System.out.print("Novo nome: ");
                                            nome = Ler.umaString();
                                            listaP.get(num-1).setNome(nome);
                                            
                                            break;
                                        case 2: //Alterar Salario Professor
                                            System.out.println("Salario Atual: " + listaP.get(num-1).getSalario());
                                            System.out.print("Novo Salario: ");
                                            float salario = Ler.umFloat();
                                            listaP.get(num-1).setSalario(salario);
                                            
                                            break;
                                        case 3: //Alterar horaio Professor
                                            System.out.println("1) Novo Horario");
                                            System.out.println("2) Apagar Horario");
                                            menu = Ler.umInt();
                                            while(menu<1 || menu>2) {
                                                System.out.print("Opção Inválida. Indique uma nova opção: ");
                                                menu = Ler.umInt();
                                            }
                                            if(menu==1){//Adicionar horario prof
                                                System.out.println("\nHorario: ");
                                                System.out.println("1) Segunda-feira");
                                                System.out.println("2) Terça-feira");
                                                System.out.println("3) Quarta-feira");
                                                System.out.println("4) Quinta-feira");
                                                System.out.println("5) Sexta-feira");
                                                System.out.print("Dia: ");
                                                dia = Ler.umInt();
                                                while(dia<1 || dia>5) {
                                                    System.out.print("Opção Inválida. Escolha uma opção válida: ");
                                                    dia = Ler.umInt();
                                                }
                                                int hora=listaP.get(num-1).mostrarHorarioDisponivel(dia);
                                                if(hora == 0) {
                                                    System.out.println("Não há mais horários disponiveis neste dia");
                                                    continue;
                                                }
                                                System.out.println("Tipo de aula: ");
                                                System.out.println("1) Condução");
                                                System.out.println("2) Código");
                                                int tipo = Ler.umInt();
                                                while(tipo < 1 || tipo > 2) {
                                                    System.out.print("Opção Inválida. Escolha uma opção válida: ");
                                                    tipo = Ler.umInt();
                                                }

                                                if(tipo == 1)
                                                    h.setTipoAula("Condução");
                                                else
                                                    h.setTipoAula("Código");
                                                h.setHora(hora);
                                                h.setDia(dia);
                                                h.setnomeP(listaP.get(num-1).getNome());

                                                listaP.get(num-1).addHorario((Horario)h.clone());
                                            }
                                            else{
                                                if(listaP.get(num-1).horario.size() <= 1) {
                                                    System.out.println("Precisa de ter pelo menos um horário");
                                                    break;
                                                }
                                                for(int i=0;i<listaP.get(num-1).horario.size();i++) {
                                                    System.out.println(i+1 + ") " + listaP.get(num-1).horario.get(i).imprimeDia() + ": " + listaP.get(num-1).horario.get(i).getHora() + "h - " + (listaP.get(num-1).horario.get(i).getHora()+2) + listaP.get(num-1).horario.get(i).getTipoAula());
                                                }
                                                System.out.print("Menu: ");
                                                menu = Ler.umInt();
                                                while(menu<=0 || menu>listaP.get(num-1).horario.size()) {
                                                    System.out.print("Opção Inválida. Indique uma nova opção: ");
                                                    menu = Ler.umInt();
                                                }
                                                listaP.get(num-1).horario.remove(menu-1);
                                                
                                            }
                                            break;
                                    }
                                }while(k!=true);
                                break;
                        }
                    }while(k!=true);
                    
                    break;
                case 4:
                    System.out.println("\n---Apagar Utilizador---");
                    System.out.println("1) Apagar Aluno");
                    System.out.println("2) Apagar Professor");
                    System.out.print("Menu: ");
                    menu = Ler.umInt();
                    while(menu<1 || menu>2) {
                        System.out.print("Opção Inválida. Indique uma nova opção: ");
                        menu = Ler.umInt();
                    }
                    
                    if(menu == 1) { //Apagar Aluno
                        do{
                            System.out.print("\nIndique o número do aluno a apagar: ");
                            num = Ler.umInt();
                            //Corrigir numero
                            b=false;
                            for(int i=0;i<listaA.size();i++){
                                if(listaA.get(i).getNumero()==num){
                                    num=i+1;
                                    b=true;
                                    break;
                                }
                            }
                            if(b==false){
                                System.out.println("Não existe um aluno com este número");

                            }
                        }while(b!=true);
                        listaA.remove(num-1);
                        
                        
                    }
                    else { //Apagar Professor
                        do{
                            System.out.print("\nIndique o número do Professor a apagar: ");
                            num = Ler.umInt();
                            //Corrigir numero
                            b=false;
                            for(int i=0;i<listaP.size();i++){
                                if(listaP.get(i).getNumero()==num){
                                    num=i+1;
                                    b=true;
                                    break;
                                }
                            }
                            if(b==false){
                                System.out.println("Não existe um Professor com este número");

                            }
                        }while(b!=true);
                        listaP.remove(num-1);   
                    }
                    break;
            }   
        }
        
        
    }
}